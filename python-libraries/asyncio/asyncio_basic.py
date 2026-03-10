import asyncio
import time


async def worker(task_name):
    print(f"start: {task_name}")
    # 非同期に2秒間スリープ
    await asyncio.sleep(2)
    print(f"end: {task_name}")

    return task_name


async def main():
    # 非同期タスクを作成する
    tasks = [
        asyncio.create_task(worker("task1")),
        asyncio.create_task(worker("task2")),
        asyncio.create_task(worker("task3")),
    ]
    # 非同期に実行完了を待ち、結果をリストで取得
    results = await asyncio.gather(*tasks)
    # 結果表示
    print("===== 結果")
    for result in results:
        print(result)


if __name__ == "__main__":
    t = time.time()
    # asyncio.runを使用してメインコルーチンを実行
    asyncio.run(main())
    # 実行時間を表示
    print(f"実行時間: {time.time() - t:.5f} sec")
