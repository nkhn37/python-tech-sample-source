import asyncio

from db_connect_asyncpg import DbConnectAsyncPostgres


async def insert_data_with_transaction(value1, value2):
    """データをインサートする (トランザクションを明示的に管理する場合)"""

    async with DbConnectAsyncPostgres() as db:
        try:
            # トランザクションの開始
            await db.start_transaction()

            # インサートを実行
            insert_sql = """
                INSERT INTO work.sample_table
                (str1, value1, last_update_datetime)
                VALUES($1, $2, current_timestamp)
            """
            await db.execute_non_query(insert_sql, (value1, value2))

            # コミット
            await db.commit_transaction()
        except Exception as ex:
            if db.transaction is not None:
                await db.rollback_transaction()
            print(f"エラー発生: {ex}")
            raise


async def main():
    # 接続プールを初期化する
    await DbConnectAsyncPostgres.initialize_connection_pool()

    try:
        # 非同期タスクを並行実行
        tasks = [
            insert_data_with_transaction(f"test_str{i}", 10 * i) for i in range(10)
        ]
        await asyncio.gather(*tasks)
    finally:
        # 接続プールをクローズする
        await DbConnectAsyncPostgres.close_connection_pool()


if __name__ == "__main__":
    # asyncio.runを使用してメインコルーチンを実行
    asyncio.run(main())
