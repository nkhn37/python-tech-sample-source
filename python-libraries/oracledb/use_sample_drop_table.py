from db_connect_oracle import DbConnectOracle


def main():
    # テーブルを削除する
    db_oracle = DbConnectOracle()

    drop_table_sql = "DROP TABLE SAMPLE_TABLE"
    db_oracle.execute_non_query(sql=drop_table_sql)


if __name__ == "__main__":
    main()
