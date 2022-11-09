"""cx_Oracleモジュール
cx_Oracleを用いたOracleデータベースへのアクセス方法

[説明ページ]
https://tech.nkhn37.net/python-cx-oracle-dbaccess/#cx_OracleOracle
"""
import cx_Oracle
import configparser


class DbConnectOracle:
    def __init__(self) -> None:
        """コンストラクタ
        :return: None
        """
        # コンフィグファイルからデータを取得
        config_db = configparser.ConfigParser()
        config_db.read("dbconfig.ini")

        # 接続情報の取得
        host = config_db["ORACLE_DB_SERVER"]["host"]
        port = config_db["ORACLE_DB_SERVER"]["port"]
        service_name = config_db["ORACLE_DB_SERVER"]["service"]
        user = config_db["ORACLE_DB_SERVER"]["user"]
        password = config_db["ORACLE_DB_SERVER"]["password"]

        # DSN(データソース名)を作成する
        self.dsn = cx_Oracle.makedsn(host, port, service_name=service_name)

        # コネクションを確立する
        self.con = cx_Oracle.connect(
            user=user, password=password, dsn=self.dsn, encoding="UTF-8"
        )

        # カーソルを作成する
        self.cursor = self.con.cursor()

    def execute_non_query(self, sql: str, bind_var: dict = None) -> None:
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

    def execute_query(self, sql: str, bind_var: dict = None, count: int = 0) -> list:
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
            columns = [col[0] for col in self.cursor.description]
            self.cursor.rowfactory = lambda *args: dict(zip(columns, args))
            rows = self.cursor.fetchall()
            for row in rows:
                result.append(row)
        else:
            # 件数指定がある場合はその件数分を取得する
            columns = [col[0] for col in self.cursor.description]
            self.cursor.rowfactory = lambda *args: dict(zip(columns, args))
            rows = self.cursor.fetchmany(count)
            for row in rows:
                result.append(row)

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
    db_oracle = DbConnectOracle()

    # ===== テーブルを作成する
    create_sql = (
        "CREATE TABLE SAMPLE_TABLE"
        "("
        "ID NUMBER GENERATED ALWAYS AS IDENTITY,"
        "STR1 VARCHAR2(50), "
        "VALUE1 NUMBER, "
        "LAST_UPDATE_DATETIME TIMESTAMP, "
        "PRIMARY KEY (ID)"
        ")"
    )
    db_oracle.execute_non_query(create_sql)
    # コミット
    db_oracle.commit()

    # ===== データをINSERTする
    insert_sql = (
        "INSERT INTO SAMPLE_TABLE "
        "(STR1, VALUE1, LAST_UPDATE_DATETIME) "
        "VALUES(:str1, :val1, CURRENT_TIMESTAMP)"
    )
    for i in range(5):
        input_str = f"test_str{i}"
        input_val = 10 * i
        bind = {"str1": input_str, "val1": input_val}
        db_oracle.execute_non_query(insert_sql, bind)
    # コミット
    db_oracle.commit()

    # ===== データを検索する (全て検索)
    print("===== 全件検索")
    select_sql = "SELECT * FROM SAMPLE_TABLE"
    select_result = db_oracle.execute_query(select_sql)
    print(select_result)

    # ===== 件数を指定して検索する (以下の例は3件)
    print("===== 取得する件数の指定")
    select_sql = "SELECT * FROM SAMPLE_TABLE"
    select_result = db_oracle.execute_query(select_sql, count=3)
    print(select_result)

    # ===== 条件を指定して検索する
    print("===== 条件を指定して実行する")
    select_sql = "SELECT * FROM SAMPLE_TABLE WHERE VALUE1 > :val1"
    print("条件１")
    select_result = db_oracle.execute_query(select_sql, {"val1": 10})
    print(select_result)
    print("条件２")
    select_result = db_oracle.execute_query(select_sql, {"val1": 30})
    print(select_result)


if __name__ == "__main__":
    main()
