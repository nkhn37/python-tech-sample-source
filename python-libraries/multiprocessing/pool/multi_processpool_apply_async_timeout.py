"""multiprocessingによるマルチプロセスの基本
プロセスプール(Pool)の使い方
プールでのプロセス実行: apply_async (timeout設定)

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#_apply_async
"""
import logging
import time
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")

# プロセスプールのサイズ
PROCESS_POOL_SIZE = 3


def myworker(x: int):
    logging.debug(f"start")
    time.sleep(5)
    logging.debug("end")

    return x


def main():
    logging.debug("start")

    # プロセスプールの生成
    with Pool(PROCESS_POOL_SIZE) as pool:
        process1 = pool.apply_async(func=myworker, args=(10,))
        process2 = pool.apply_async(func=myworker, args=(20,))
        process3 = pool.apply_async(func=myworker, args=(30,))
        process4 = pool.apply_async(func=myworker, args=(40,))
        process5 = pool.apply_async(func=myworker, args=(50,))

        logging.debug("execute async")

        # 実行結果を取得
        logging.debug(process1.get(timeout=1))
        logging.debug(process2.get())
        logging.debug(process3.get())
        logging.debug(process4.get())
        logging.debug(process5.get())

    logging.debug("end")


if __name__ == "__main__":
    main()
