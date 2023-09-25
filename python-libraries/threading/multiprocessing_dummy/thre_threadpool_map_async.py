"""multiprocessing.dummyを使ったマルチスレッドプール
Threadingモジュールではないが、multiprocessingモジュールにあるPoolを
ThreadPoolとして使うことができる

[説明ページ]

"""
import logging
import time
from multiprocessing.dummy import Pool as ThreadPool

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

# スレッドプールのサイズ
THREAD_POOL_SIZE = 3


def myworker(x: int):
    logging.debug("start")

    time.sleep(1)
    logging.debug(x)

    logging.debug("end")


def main():
    logging.debug("start")

    # 表示したい値のリスト
    vals = [i for i in range(10)]

    # スレッドプールの使用
    with ThreadPool(THREAD_POOL_SIZE) as pool:
        results = pool.map_async(myworker, vals)

        # map_asyncは非同期なので↓はすぐに表示
        logging.debug("execute")

        # getを実行したら動作する
        logging.debug(results)
        results.get()

    logging.debug("end")


if __name__ == "__main__":
    main()
