"""multiprocessingによるマルチプロセスの基本
マルチスレッドとマルチプロセスのメモリの扱いの違い
(マルチプロセスではプロセス間でメモリは共有されないことの確認)

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#i-3
"""
import logging
from multiprocessing import Process

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def myworker(data: dict):
    logging.debug("start")
    data["x"] += 1
    logging.debug(f"end: {data}, {id(data)}")


def main():
    logging.debug("start")

    # データを用意
    data = {"x": 0}

    # プロセスを生成
    process1 = Process(target=myworker, args=(data,))
    process2 = Process(target=myworker, args=(data,))

    # プロセスの開始
    process1.start()
    process2.start()

    # プロセスの終了を待機
    process1.join()
    process2.join()

    logging.debug(f"end: {data}, {id(data)}")


if __name__ == "__main__":
    main()
