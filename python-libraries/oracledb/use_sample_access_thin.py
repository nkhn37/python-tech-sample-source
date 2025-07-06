from db_connect_oracle import DbConnectOracle


def main():
    # Thin モードでアクセスする場合
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
