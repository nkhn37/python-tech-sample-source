"""multiprocessingによるマルチプロセスの基本
基本的な使い方 Process

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#_Process
"""
import logging
import os
import time
from multiprocessing import Process

logging.basicConfig(
    level=logging.DEBUG, format="%(processName)s_%(threadName)s: %(message)s"
)


def myworker1():
    logging.debug(f"start (pid:{os.getpid()})")
    time.sleep(5)
    logging.debug(f"end (pid:{os.getpid()})")


def myworker2():
    logging.debug(f"start (pid:{os.getpid()})")
    time.sleep(5)
    logging.debug(f"end (pid:{os.getpid()})")


def main():
    logging.debug(f"start (pid:{os.getpid()})")

    # プロセスの生成
    process1 = Process(target=myworker1)
    process2 = Process(target=myworker2)

    # プロセスの開始
    process1.start()
    process2.start()

    # プロセスの終了を待機
    process1.join()
    process2.join()

    logging.debug(f"end (pid:{os.getpid()})")


if __name__ == "__main__":
    main()
