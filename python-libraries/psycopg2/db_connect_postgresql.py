"""psycopg2モジュール
psycopg2を用いたPostgreSQLデータベースへのアクセス方法

[説明ページ]
https://tech.nkhn37.net/python-psycopg2-postgresql-dbaccess/#psycopg2PostgreSQL
"""
import configparser

import psycopg2
import psycopg2.extras
from psycopg2 import pool


class DbConnectPostgres:
    # 接続プール
    connection_pool = None

    @classmethod
    def initialize_connection_pool(cls, config_file="./dbconfig.ini") -> None:
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
            minconn = int(config_db["POOL"]["minconn"])
            maxconn = int(config_db["POOL"]["maxconn"])

            # 接続プールを初期化
            cls.connection_pool = pool.ThreadedConnectionPool(
                minconn=minconn,
                maxconn=maxconn,
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password,
            )

    @classmethod
    def close_connection_pool(cls):
        """接続プールをクローズする"""
        if cls.connection_pool:
            cls.connection_pool.closeall()
            cls.connection_pool = None

    def __init__(self) -> None:
        """コンストラクタ"""
        # コネクションとカーソル
        self.conn = None
        self.cursor = None

    def connect(self) -> None:
        """DB接続"""
        if self.connection_pool is None:
            raise Exception("接続プールが初期化されていません")

        # 接続プールからコネクションを取得
        self.conn = self.connection_pool.getconn()
        # カーソルを取得
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.DictCursor
        )

    def close(self) -> None:
        """DBクローズ"""
        if self.cursor:
            # カーソルをクローズする
            self.cursor.close()
            self.cursor = None
        if self.conn:
            # 接続をプールに返却する
            self.connection_pool.putconn(self.conn)
            self.conn = None

    def __enter__(self):
        # DB接続
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # 例外発生時はロールバック
            self.rollback()
            raise
        else:
            # 例外がなければコミット
            self.commit()

        # DBクローズ
        self.close()

    def execute_non_query(self, sql: str, bind_var: tuple = None) -> None:
        """CREATE/INSERT/UPDATE/DELETEのSQL実行メソッド

        Args:
            sql: 実行SQL
            bind_var: バインド変数

        Returns:
            None
        """
        # SQLの実行
        if bind_var:
            # バインド変数がある場合は指定して実行
            self.cursor.execute(sql, bind_var)
        else:
            self.cursor.execute(sql)

    def execute_query(
        self, sql: str, bind_var: tuple = None, count: int = 0
    ) -> list[psycopg2.extras.DictRow]:
        """SELECTのSQL実行メソッド

        Args:
            sql: 実行SQL
            bind_var: バインド変数
            count: データ取得件数

        Returns:
            結果リスト
        """
        # SQLの実行
        if bind_var:
            # バインド変数がある場合は指定して実行
            self.cursor.execute(sql, bind_var)
        else:
            self.cursor.execute(sql)

        if count == 0:
            rows = self.cursor.fetchall()
        else:
            # 件数指定がある場合はその件数分を取得する
            rows = self.cursor.fetchmany(count)

        return rows

    def commit(self) -> None:
        """コミット"""
        self.conn.commit()

    def rollback(self) -> None:
        """ロールバック"""
        self.conn.rollback()
