import configparser

import asyncpg


class DbConnectAsyncPostgres:
    # 接続プール
    connection_pool = None

    @classmethod
    async def initialize_connection_pool(cls, config_file="./dbconfig.ini") -> None:
        """接続プールの初期化

        Args:
            config_file: 設定ファイルパス

        Returns:
            None
        """
        if cls.connection_pool is None:
            # コンフィグファイルからデータを取得
            config_db = configparser.ConfigParser()
            config_db.read(config_file)

            # 接続情報の取得
            host = config_db["POSTGRESQL_DB_SERVER"]["host"]
            port = config_db["POSTGRESQL_DB_SERVER"]["port"]
            dbname = config_db["POSTGRESQL_DB_SERVER"]["dbname"]
            user = config_db["POSTGRESQL_DB_SERVER"]["user"]
            password = config_db["POSTGRESQL_DB_SERVER"]["password"]
            # プール設定の取得
            min_size = int(config_db["POOL"]["min_size"])
            max_size = int(config_db["POOL"]["max_size"])

            # DSN(Data Source Name)の作成
            dsn = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
            # 非同期接続プールの初期化
            cls.connection_pool = await asyncpg.create_pool(
                dsn=dsn,
                min_size=min_size,
                max_size=max_size,
            )

    @classmethod
    async def close_connection_pool(cls):
        """接続プールをクローズする"""
        if cls.connection_pool:
            await cls.connection_pool.close()
            cls.connection_pool = None

    def __init__(self) -> None:
        """コンストラクタ"""
        self.conn = None
        self.transaction = None

    async def connect(self) -> None:
        """DB接続"""
        if self.__class__.connection_pool is None:
            raise RuntimeError("接続プールが初期化されていません。")

        # 接続プールから非同期でコネクションを取得
        self.conn = await self.__class__.connection_pool.acquire()

    async def close(self) -> None:
        """DBクローズ"""
        if self.conn:
            # 接続プールに返却する
            await self.__class__.connection_pool.release(self.conn)
            self.conn = None

    async def __aenter__(self):
        # DB接続
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # DBクローズ
        await self.close()

    async def execute_non_query(self, sql: str, bind_var: tuple = None) -> None:
        """CREATE / INSERT / UPDATE / DELETEの SQL 実行メソッド

        Args:
            sql: 実行SQL
            bind_var: バインド変数

        Returns:
            None
        """
        # SQLの実行 (bind_varがNoneの場合は()を設定し、アンパックして渡す)
        await self.conn.execute(sql, *(bind_var or ()))

    async def execute_query(
        self, sql: str, bind_var: tuple = None
    ) -> list[asyncpg.Record]:
        """SELECT の SQL 実行メソッド

        Args:
            sql: 実行 SQL
            bind_var: バインド変数

        Returns:
            結果リスト (asyncpg.Record型)
        """
        return await self.conn.fetch(sql, *(bind_var or ()))

    async def execute_query_one(
        self, sql: str, bind_var: tuple = None
    ) -> asyncpg.Record | None:
        """SELECT の SQL 実行メソッド（1件取得）

        Args:
            sql: 実行 SQL
            bind_var: バインド変数

        Returns:
            結果 (asyncpg.Record型)
        """
        return await self.conn.fetchrow(sql, *(bind_var or ()))

    async def start_transaction(self) -> None:
        """トランザクションの開始"""
        # コネクションでトランザクションを開始する
        self.transaction = self.conn.transaction()
        # トランザクションを開始する
        await self.transaction.start()

    async def commit_transaction(self) -> None:
        """トランザクションのコミット"""
        await self.transaction.commit()

    async def rollback_transaction(self) -> None:
        """トランザクションのロールバック"""
        await self.transaction.rollback()
