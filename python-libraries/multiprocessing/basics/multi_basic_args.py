"""multiprocessingによるマルチプロセスの基本
プロセスで動作する関数への引数の渡し方

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#i-2
"""
import logging
import time
from multiprocessing import Process

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def myworker1(x: int, y: int):
    logging.debug("start")
    logging.debug(f"x: {x}, y: {y}")
    time.sleep(5)
    logging.debug("end")


def myworker2():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def main():
    logging.debug("start")

    # プロセスの生成
    process1 = Process(target=myworker1, args=(10,), kwargs={"y": 20})
    process2 = Process(target=myworker2)

    # プロセスの開始
    process1.start()
    process2.start()

    # プロセスの終了を待機
    process1.join()
    process2.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
