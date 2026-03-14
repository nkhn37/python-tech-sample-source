import asyncio

from db_connect_asyncpg import DbConnectAsyncPostgres


async def insert_data_with_auto_commit(value1, value2):
    """データをインサートする (自動コミットモードを使用する場合)"""
    async with DbConnectAsyncPostgres() as db:
        insert_sql = """
            INSERT INTO work.sample_table
            (str1, value1, last_update_datetime)
            VALUES($1, $2, current_timestamp)
        """

        await db.execute_non_query(insert_sql, (value1, value2))


async def main():
    # 接続プールを初期化する
    await DbConnectAsyncPostgres.initialize_connection_pool()

    try:
        # 非同期タスクを並行実行
        tasks = [
            insert_data_with_auto_commit(f"test_str{i}", 10 * i) for i in range(10)
        ]
        await asyncio.gather(*tasks)
    finally:
        # 接続プールをクローズする
        await DbConnectAsyncPostgres.close_connection_pool()


if __name__ == "__main__":
    # asyncio.runを使用してメインコルーチンを実行
    asyncio.run(main())
