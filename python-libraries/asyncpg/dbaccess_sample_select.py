import asyncio
from pprint import pprint

from db_connect_asyncpg import DbConnectAsyncPostgres


async def select_data(min_value):
    """データを検索する"""
    async with DbConnectAsyncPostgres() as db:
        select_sql = """
            SELECT id, str1, value1, last_update_datetime
            FROM work.sample_table
            WHERE value1 >= $1
            ORDER BY id
        """
        result = await db.execute_query(select_sql, (min_value,))

        return result


async def main():
    # 接続プールを初期化する
    await DbConnectAsyncPostgres.initialize_connection_pool()

    try:
        # 非同期タスクを並行実行
        tasks = [
            select_data(0),
            select_data(20),
            select_data(50),
        ]
        results = await asyncio.gather(*tasks)
        pprint(results)
    finally:
        # 接続プールをクローズする
        await DbConnectAsyncPostgres.close_connection_pool()


if __name__ == "__main__":
    # asyncio.runを使用してメインコルーチンを実行
    asyncio.run(main())
