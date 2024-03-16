"""psycopg2モジュール
psycopg2を用いたPostgreSQLデータベースへのアクセス方法

[説明ページ]
https://tech.nkhn37.net/python-psycopg2-postgresql-dbaccess/#psycopg2PostgreSQL
"""
import configparser

import psycopg2
import psycopg2.extras


class DbConnectPostgres:
    def __init__(self, config_file="./dbconfig.ini") -> None:
        """コンストラクタ"""
        # コネクションとカーソル
        self.conn = None
        self.cursor = None

        # コンフィグファイルからデータを取得
        config_db = configparser.ConfigParser()
        config_db.read(config_file)

        # 接続情報の取得
        self.host = config_db["POSTGRESQL_DB_SERVER"]["host"]
        self.port = config_db["POSTGRESQL_DB_SERVER"]["port"]
        self.dbname = config_db["POSTGRESQL_DB_SERVER"]["dbname"]
        self.user = config_db["POSTGRESQL_DB_SERVER"]["user"]
        self.password = config_db["POSTGRESQL_DB_SERVER"]["password"]

    def connect(self) -> None:
        """DB接続"""
        # コネクション確立
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password,
        )

        # カーソル作成
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.DictCursor
        )

    def close(self) -> None:
        """DBクローズ"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def __enter__(self):
        # DB接続
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            # 例外発生時はロールバック
            self.rollback()
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
