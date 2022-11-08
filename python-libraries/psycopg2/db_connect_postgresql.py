"""psycopg2モジュール
psycopg2を用いたPostgreSQLデータベースへのアクセス方法

[説明ページ]
https://tech.nkhn37.net/python-psycopg2-postgresql-dbaccess/#psycopg2PostgreSQL
"""
import psycopg2
import psycopg2.extras
import configparser


class DbConnectPostgres:
    def __init__(self) -> None:
        """コンストラクタ
        :return: None
        """
        # コンフィグファイルからデータを取得
        config_db = configparser.ConfigParser()
        config_db.read("./dbconfig.ini")

        # 接続情報の取得
        host = config_db["POSTGRESQL_DB_SERVER"]["host"]
        port = config_db["POSTGRESQL_DB_SERVER"]["port"]
        dbname = config_db["POSTGRESQL_DB_SERVER"]["dbname"]
        user = config_db["POSTGRESQL_DB_SERVER"]["user"]
        password = config_db["POSTGRESQL_DB_SERVER"]["password"]

        # コネクションを確立する
        self.con = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password
        )
        self.con.set_client_encoding("utf-8")

        # カーソルを作成する
        self.cursor = self.con.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def execute_non_query(self, sql: str, bind_var: tuple = None) -> None:
        """CREATE/INSERT/UPDATE/DELETEのSQL実行メソッド
        :param sql: 実行SQL
        :param bind_var: バインド変数
        :return: None
        """
        # SQLの実行
        if bind_var is None:
            self.cursor.execute(sql)
        else:
            # バインド変数がある場合は指定して実行
            self.cursor.execute(sql, bind_var)

    def execute_query(self, sql: str, bind_var: tuple = None, count: int = 0) -> list:
        """SELECTのSQL実行メソッド
        :param sql: 実行SQL
        :param bind_var: バインド変数
        :param count: データ取得件数
        :return: 結果リスト
        """
        # SQLの実行
        if bind_var is None:
            self.cursor.execute(sql)
        else:
            # バインド変数がある場合は指定して実行
            self.cursor.execute(sql, bind_var)

        result = []
        if count == 0:
            rows = self.cursor.fetchall()
            for row in rows:
                result.append(dict(row))
        else:
            # 件数指定がある場合はその件数分を取得する
            rows = self.cursor.fetchmany(count)
            for row in rows:
                result.append(dict(row))

        return result

    def commit(self) -> None:
        """コミット
        :return: None
        """
        self.con.commit()

    def rollback(self) -> None:
        """ロールバック
        :return: None
        """
        self.con.rollback()

    def __del__(self) -> None:
        """デストラクタ
        :return: None
        """
        self.cursor.close()
        self.con.close()


def main():
    db_postgre = DbConnectPostgres()

    # ===== テーブルを作成する
    create_sql = (
        "CREATE TABLE IF NOT EXISTS work.sample_table"
        "("
        "id serial NOT NULL, "
        "str1 character varying(50), "
        "value1 integer, "
        "last_update_datetime timestamp, "
        "PRIMARY KEY (id)"
        ")"
    )
    db_postgre.execute_non_query(create_sql)
    # コミット
    db_postgre.commit()

    # ===== データをINSERTする
    insert_sql = (
        "INSERT INTO work.sample_table "
        "(str1, value1, last_update_datetime) "
        "VALUES(%s, %s, current_timestamp)"
    )
    for i in range(5):
        input_str = f"test_str{i}"
        input_val = 10 * i
        bind = (input_str, input_val)
        db_postgre.execute_non_query(insert_sql, bind)
    # コミット
    db_postgre.commit()

    # ===== データを検索する (全て検索)
    print("===== 全件検索")
    select_sql = "SELECT * FROM work.sample_table"
    select_result = db_postgre.execute_query(select_sql)
    print(select_result)

    # ===== 件数を指定して検索する (以下の例は3件)
    print("===== 取得する件数の指定")
    select_sql = "SELECT * FROM work.sample_table"
    select_result = db_postgre.execute_query(select_sql, count=3)
    print(select_result)

    # ===== 条件を指定して検索する
    print("===== 条件を指定して実行する")
    select_sql = "SELECT * FROM work.sample_table WHERE value1 > %s"
    print("条件１")
    select_result = db_postgre.execute_query(select_sql, (10,))
    print(select_result)
    print("条件２")
    select_result = db_postgre.execute_query(select_sql, (30,))
    print(select_result)


if __name__ == "__main__":
    main()
