"""threadingによるマルチスレッド処理の基本
キューを用いたスレッド制御

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#_queueQueue
"""
import logging
import time
from queue import Empty, Queue
from threading import Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

# スレッドプールのサイズ
THREAD_POOL_SIZE = 3


def myworker(work_queue):
    logging.debug("start")

    # キューが空でない限り繰り返す
    while not work_queue.empty():
        try:
            item = work_queue.get_nowait()
        except Empty:
            break
        else:
            time.sleep(1)
            logging.debug(item)
            # タスク終了 ↓を書かないとwork_queue.join()で終了を区別できない
            work_queue.task_done()

    logging.debug("end")


def main():
    logging.debug("start")

    # スレッドで共有するキューを用意する
    work_queue = Queue()

    # 表示したい値のリスト
    vals = [i for i in range(10)]
    # キューに投入する
    for val in vals:
        work_queue.put(val)

    # スレッドプール数のスレッドを用意
    threads = [
        Thread(target=myworker, args=(work_queue,))
        for _ in range(THREAD_POOL_SIZE)
    ]

    # スレッドの開始
    for thread in threads:
        thread.start()

    # キューが空になるまで待機
    work_queue.join()

    # 終了を待機
    for thread in threads:
        thread.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
