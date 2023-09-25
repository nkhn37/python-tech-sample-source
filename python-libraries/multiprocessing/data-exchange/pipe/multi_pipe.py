"""multiprocessingによるマルチプロセスの基本
プロセス間のデータ交換方法
Pipeでのデータ交換

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#Pipe
"""
import logging
from multiprocessing import Pipe, Process

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


class CustomClass:
    pass


def myworker(conn):
    logging.debug("child: start")

    # 送信データの用意
    data = [1, "string", {"dict": 0}, CustomClass()]
    logging.debug(f"child: {data}")

    # 親プロセスへデータを送信
    conn.send(data)
    # コネクションをクローズ
    conn.close()

    logging.debug("child: end")


def main():
    logging.debug("parent: start")

    # 親コネクションと子コネクションを生成
    # 引数指定しない場合は、デフォルトはPipe(duplex=True)で双方向になっている
    # Pipe(duplex=False)にするとparrent_conn:受信専用、child_conn:送信専用になる
    parent_conn, child_conn = Pipe()

    child_process = Process(target=myworker, args=(child_conn,))

    # 子プロセスの開始
    child_process.start()

    # 子プロセスからのデータを受信
    data = parent_conn.recv()
    logging.debug(f"parent: {data}")

    # プロセスの終了を待機
    child_process.join()

    logging.debug("parent: end")


if __name__ == "__main__":
    main()
