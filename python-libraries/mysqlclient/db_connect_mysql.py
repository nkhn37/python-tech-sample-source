"""mysqlclientモジュール
mysqlclientを用いたMySQLデータベースへのアクセス方法

[説明ページ]
https://tech.nkhn37.net/python-mysqlclient-dbaccess/#mysqlclientMySQL
"""
"""DBアクセス (MySQL)
"""
import MySQLdb
import configparser


class DbConnectMySQL:
    def __init__(self) -> None:
        """コンストラクタ
        :return:
        """
        # コンフィグファイルからデータを取得
        config_db = configparser.ConfigParser()
        config_db.read("dbconfig.ini")

        # 接続情報の取得
        host = config_db["MYSQL_DB_SERVER"]["host"]
        port = int(config_db["MYSQL_DB_SERVER"]["port"])
        dbname = config_db["MYSQL_DB_SERVER"]["dbname"]
        user = config_db["MYSQL_DB_SERVER"]["user"]
        password = config_db["MYSQL_DB_SERVER"]["password"]

        # コネクションを確立する
        self.con = MySQLdb.connect(
            host=host, port=port, user=user, passwd=password, db=dbname
        )

        # カーソルを作成する
        self.cursor = self.con.cursor(MySQLdb.cursors.DictCursor)

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
                result.append(row)
        else:
            # 件数指定がある場合はその件数分を取得する
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
        :return:
        """
        self.cursor.close()
        self.con.close()


def main():
    db_mysql = DbConnectMySQL()

    # ===== テーブルを作成する
    create_sql = (
        "CREATE TABLE IF NOT EXISTS sample_table"
        "("
        "id INT NOT NULL AUTO_INCREMENT, "
        "str1 VARCHAR(50), "
        "value1 INT, "
        "last_update_datetime TIMESTAMP, "
        "PRIMARY KEY (id)"
        ")"
    )
    db_mysql.execute_non_query(create_sql)
    # コミット
    db_mysql.commit()

    # ===== データをINSERTする
    insert_sql = (
        "INSERT INTO sample_table "
        "(str1, value1, last_update_datetime) "
        "VALUES(%s, %s, CURRENT_TIMESTAMP)"
    )
    for i in range(5):
        input_str = f"test_str{i}"
        input_val = 10 * i
        bind = (input_str, input_val)
        db_mysql.execute_non_query(insert_sql, bind)
    # コミット
    db_mysql.commit()

    # ===== データを検索する (全て検索)
    print("===== 全件検索")
    select_sql = "SELECT * FROM sample_table"
    select_result = db_mysql.execute_query(select_sql)
    print(select_result)

    # ===== 件数を指定して検索する (以下の例は3件)
    print("===== 取得する件数の指定")
    select_sql = "SELECT * FROM sample_table"
    select_result = db_mysql.execute_query(select_sql, count=3)
    print(select_result)

    # ===== 条件を指定して検索する
    print("===== 条件を指定して実行する")
    select_sql = "SELECT * FROM sample_table WHERE value1 > %s"
    print("条件１")
    select_result = db_mysql.execute_query(select_sql, (10,))
    print(select_result)
    print("条件２")
    select_result = db_mysql.execute_query(select_sql, (30,))
    print(select_result)


if __name__ == "__main__":
    main()
