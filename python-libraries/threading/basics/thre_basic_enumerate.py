"""threadingによるマルチスレッド処理の基本
実行しているスレッド数の確認

[説明ページ]

"""
import logging
import threading
import time
from threading import Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def myworker():
    logging.debug("start")
    time.sleep(5)
    logging.debug("end")


if __name__ == "__main__":
    logging.debug("start")

    # 複数のスレッドを生成 (デーモン)
    for _ in range(5):
        t = Thread(target=myworker)
        t.daemon = True
        t.start()

    # enumerateで生存中スレッドを確認
    logging.debug(threading.enumerate())

    # enumerateで生存中スレッドを取り出しjoinを実行
    for thread in threading.enumerate():
        # メインスレッドはjoin不要
        if thread is threading.current_thread():
            continue
        # 各スレッドに対するjoinを実行
        thread.join()

    logging.debug("end")
