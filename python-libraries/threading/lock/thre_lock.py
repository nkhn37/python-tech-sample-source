"""threadingによるマルチスレッド処理の基本
ロックの取得 Lock

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#_Lock
"""
import logging
import time
from threading import Lock, Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def mycounter(d: dict, lock: Lock):
    # ロックを取得
    with lock:
        logging.debug("start")

        tmp = d["x"]
        time.sleep(1)
        d["x"] = tmp + 1

        logging.debug(f"end {d}")

    # # with句を使わない場合の以下と同じ
    # # ロックを取得
    # lock.acquire()
    # # 以下のブロックがロックされる
    # tmp = d["x"]
    # time.sleep(1)
    # d["x"] = tmp + 1
    # # ロックをリリース
    # lock.release()


def main():
    logging.debug("start")
    data = {"x": 0}

    # ロックを生成
    lock = Lock()

    # スレッドの生成
    thread_num = 5
    threads = [
        Thread(target=mycounter, args=(data, lock)) for _ in range(thread_num)
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
