"""multiprocessingによるマルチプロセスの基本
プロセス間におけるデータの共有
サーバープロセス管理: Manager
Value, Arrayより簡単だが遅いため、速度を求めるならValue, Arrayの使用が適切

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#Manager
"""
import logging
from multiprocessing import Manager, Process

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def myworker(tmp_l, tmp_d, tmp_n):
    logging.debug("start")
    tmp_l.reverse()
    tmp_d["x"] += 1
    tmp_n.y *= 2

    logging.debug(tmp_l)
    logging.debug(tmp_d)
    logging.debug(tmp_n)

    logging.debug("end")


def main():
    logging.debug("start")

    with Manager() as manager:
        tmp_l = manager.list()
        tmp_d = manager.dict()
        tmp_n = manager.Namespace()

        # 値を設定
        tmp_l.append(1)
        tmp_l.append(2)
        tmp_l.append(3)
        tmp_d["x"] = 0
        tmp_n.y = 1

        # 実行前の値
        logging.debug(tmp_l)
        logging.debug(tmp_d)
        logging.debug(tmp_n)

        p = Process(target=myworker, args=(tmp_l, tmp_d, tmp_n))
        p.start()
        p.join()

        # 実行後の値
        logging.debug(tmp_l)
        logging.debug(tmp_d)
        logging.debug(tmp_n)

    logging.debug("end")


if __name__ == "__main__":
    main()
