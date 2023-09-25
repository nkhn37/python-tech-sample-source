"""multiprocessingによるマルチプロセスの基本
プロセスプール(Pool)の使い方
イテラブルな引数の使用(遅延評価版): imap

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#_imap
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

    return x * 2


def main():
    logging.debug("start")

    values = [i for i in range(1, 6)]
    logging.debug(values)

    # プロセスプールの生成
    with Pool(PROCESS_POOL_SIZE) as pool:
        # imapでイテレータを生成
        process_iter = pool.imap(func=myworker, iterable=values)
        # ここではイテレータが取得されるだけ
        logging.debug(process_iter)

        logging.debug("execute")

        # 使用するときにイテレータから読みだして実行 (遅延評価)
        for i in process_iter:
            logging.debug(i)

    logging.debug("end")


if __name__ == "__main__":
    main()
