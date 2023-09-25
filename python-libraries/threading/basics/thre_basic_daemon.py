"""threadingによるマルチスレッド処理の基本
デーモンとしてのスレッド実行方法

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#i-3
"""
import logging
import time
from threading import Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def myworker1():
    logging.debug("start")
    time.sleep(10)
    logging.debug("end")


def myworker2():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def main():
    logging.debug("start")

    # スレッドの生成
    # thread1をデーモンに設定
    thread1 = Thread(target=myworker1, daemon=True)
    # thread2はそのまま
    thread2 = Thread(target=myworker2)

    # スレッドの開始
    thread1.start()
    thread2.start()

    # スレッドの終了まで待機
    # thread1.join()
    thread2.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
