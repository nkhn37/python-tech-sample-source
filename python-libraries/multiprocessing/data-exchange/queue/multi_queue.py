"""multiprocessingによるマルチプロセスの基本
プロセス間のデータ交換方法
Queueでのデータ交換

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#Queue
"""
import logging
import time
from multiprocessing import Process, Queue
from queue import Empty

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")

# プロセスプールのサイズ
PROCESS_POOL_SIZE = 3


def myworker(work_queue):
    logging.debug("start")

    # キューが空でない限り繰り返す
    while not work_queue.empty():
        try:
            item = work_queue.get()
        except Empty:
            break
        else:
            time.sleep(1)
            logging.debug(item)

    logging.debug("end")


def main():
    logging.debug("start")

    # プロセスで共有するキューを用意する
    work_queue = Queue()

    # 表示したい値のリスト
    vals = [i for i in range(10)]
    # キューに投入する
    for val in vals:
        work_queue.put(val)

    # プロセスプール数のプロセスを用意
    processes = [
        Process(target=myworker, args=(work_queue,))
        for _ in range(PROCESS_POOL_SIZE)
    ]

    # プロセスの開始
    for process in processes:
        process.start()

    # 終了を待機
    for process in processes:
        process.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
