"""threadingによるマルチスレッド処理の基本
入れ子のロックの取得 Lock

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#_RLock
"""
import logging
import time
from threading import RLock, Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def mycounter(d: dict, lock: RLock):
    # ロックを取得
    with lock:
        logging.debug("start")

        tmp = d["x"]
        time.sleep(1)
        d["x"] = tmp + 1
        # ロック内で再度ロックを取得する
        with lock:
            tmp = d["x"]
            time.sleep(1)
            d["x"] = tmp + 1

        logging.debug(f"end {d}")


def main():
    logging.debug("start")
    data = {"x": 0}

    # ロックを生成
    lock = RLock()

    # スレッドの生成
    thread_num = 5
    threads = [
        Thread(target=mycounter, args=(data, lock)) for _ in range(thread_num)
    ]

    # スレッドの開始
    for thread in threads:
        thread.start()
    # 終了を待機
    for thread in threads:
        thread.join()

    logging.debug(data)
    logging.debug("end")


if __name__ == "__main__":
    main()
