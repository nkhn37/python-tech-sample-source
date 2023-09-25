"""threadingによるマルチスレッド処理の基本
コンディション Condition
(あるスレッドの結果を待ってから別スレッドを開始 ※ロック付き)

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#_Condition
"""
import logging
import time
from threading import Condition, Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def myworker(condition: Condition):
    with condition:
        # condition.notify_all()を待機
        condition.wait()

        logging.debug("start")
        time.sleep(5)
        logging.debug("end")


def condition_trigger(condition: Condition):
    with condition:
        logging.debug("start")
        time.sleep(5)
        logging.debug("end")

        # wait状態のスレッドを起動
        condition.notify_all()


def main():
    logging.debug("start")

    # コンディションを生成
    condition = Condition()

    # スレッドを生成
    trigger_thread = Thread(target=condition_trigger, args=(condition,))
    thread_num = 3
    threads = [
        Thread(target=myworker, args=(condition,)) for _ in range(thread_num)
    ]

    # トリガーとなるスレッド実行後に起動するスレッドを開始
    for thread in threads:
        thread.start()

    # トリガーとなるスレッドを開始
    trigger_thread.start()

    # スレッドの終了を待機
    trigger_thread.join()
    for thread in threads:
        thread.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
