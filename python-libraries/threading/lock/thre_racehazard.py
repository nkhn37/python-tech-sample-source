"""threadingによるマルチスレッド処理の基本
競合状態(race hazard または race condition)が起こる状況例

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#_RLock
"""
import logging
import time
from threading import Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def mycounter(d):
    logging.debug("start")

    tmp = d["x"]
    time.sleep(5)
    d["x"] = tmp + 1

    logging.debug(f"end {d}")


def main():
    logging.debug("start")
    data = {"x": 0}

    # スレッドの生成
    thread_num = 5
    threads = [
        Thread(target=mycounter, args=(data,)) for _ in range(thread_num)
    ]

    # スレッドの開始
    for thread in threads:
        thread.start()

    # スレッドの終了まで待機
    for thread in threads:
        thread.join()

    logging.debug(data)
    logging.debug("end")


if __name__ == "__main__":
    main()
