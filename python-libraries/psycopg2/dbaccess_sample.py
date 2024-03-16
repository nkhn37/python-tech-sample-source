"""psycopg2モジュール
実装したDbConnectPostgresクラスの使用方法

[説明ページ]
https://tech.nkhn37.net/python-psycopg2-postgresql-dbaccess/#DB
"""
from db_connect_postgresql import DbConnectPostgres


def main():
    with DbConnectPostgres() as db:
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
        db.execute_non_query(create_sql)

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
            db.execute_non_query(insert_sql, bind)

        # ===== データを検索する (全て検索)
        print("===== 全件検索")
        select_sql = "SELECT * FROM work.sample_table"
        select_result = db.execute_query(select_sql)
        print(select_result)

        # ===== 件数を指定して検索する (以下の例は3件)
        print("===== 取得する件数の指定")
        select_sql = "SELECT * FROM work.sample_table"
        select_result = db.execute_query(select_sql, count=3)
        print(select_result)

        # ===== 条件を指定して検索する
        print("===== 条件を指定して実行する")
        select_sql = "SELECT * FROM work.sample_table WHERE value1 > %s"
        print("条件１")
        select_result = db.execute_query(select_sql, (10,))
        print(select_result)
        print("条件２")
        select_result = db.execute_query(select_sql, (30,))
        print(select_result)


if __name__ == "__main__":
    main()
