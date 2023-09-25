"""multiprocessingによるマルチプロセスの基本
プロセスプール(Pool)の使い方
イテラブルな引数の使用(非同期版): map_async (timeout設定)

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#_map_async
"""
import logging
import time
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")

# プロセスプールのサイズ
PROCESS_POOL_SIZE = 3


def myworker(x: int):
    logging.debug(f"start")
    time.sleep(5)
    logging.debug("end")

    return x * 2


def main():
    logging.debug("start")

    values = [i for i in range(1, 6)]
    logging.debug(values)

    # プロセスプールの生成
    with Pool(PROCESS_POOL_SIZE) as pool:
        # map_asyncで非同期に実行
        result = pool.map_async(func=myworker, iterable=values)

        # 非同期なのですぐ表示される
        logging.debug("execute async")

        # 実行結果を表示
        logging.debug(result.get(timeout=1))

    logging.debug("end")


if __name__ == "__main__":
    main()
