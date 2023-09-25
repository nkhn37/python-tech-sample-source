"""multiprocessingによるマルチプロセスの基本
プロセス名称をつけたい場合

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#i
"""
import logging
import time
from multiprocessing import Process

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def myworker1():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def myworker2():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


def main():
    logging.debug("start")

    # プロセスの生成
    process1 = Process(target=myworker1, name="myworker1_process")
    process2 = Process(target=myworker2, name="myworker2_process")

    # プロセスの開始
    process1.start()
    process2.start()

    # プロセスの終了を待機
    process1.join()
    process2.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
