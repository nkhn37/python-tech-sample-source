"""threadingによるマルチスレッド処理の基本
タイマーを用いたスレッド実行 Timer

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#i-4
"""
import logging
import time
from threading import Timer

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def myworker(x: int, y: int):
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def main():
    logging.debug("start")

    # タイマーで5秒後に実行開始
    thread = Timer(5, myworker, args=(10,), kwargs={"y": 20})

    # スレッドの開始
    thread.start()

    # スレッドの終了まで待機
    thread.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
