"""multiprocessingによるマルチプロセスの基本
マルチスレッドとマルチプロセスのメモリの扱いの違い
(マルチスレッドではメモリが共有されることの確認)

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#i-3
"""
import logging
from threading import Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def myworker(data: dict):
    logging.debug("start")
    data["x"] += 1
    logging.debug(f"end: {data}, {id(data)}")


def main():
    logging.debug("start")

    # データを用意
    data = {"x": 0}

    # スレッドを生成
    thread1 = Thread(target=myworker, args=(data,))
    thread2 = Thread(target=myworker, args=(data,))

    # スレッドの開始
    thread1.start()
    thread2.start()

    # スレッドの終了を待機
    thread1.join()
    thread2.join()

    logging.debug(f"end: {data}, {id(data)}")


if __name__ == "__main__":
    main()
