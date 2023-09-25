"""threadingによるマルチスレッド処理の基本
BoundedSemaphoreの使用例

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#_BoundedSemaphore
"""
import logging
import sqlite3
from threading import BoundedSemaphore, Thread

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def dbaccess(dbname: str, sema: BoundedSemaphore):
    # セマフォを使用
    with sema:
        logging.debug("start")

        # DB接続
        conn = sqlite3.connect(dbname)
        curs = conn.cursor()

        # DBを検索
        select_all_sql = "SELECT * FROM person"
        curs.execute(select_all_sql)
        rows = curs.fetchall()

        # DBをクローズ
        curs.close()
        conn.close()
        logging.debug(f"end: {rows}")


def main():
    logging.debug("start")

    # データベース名
    dbname = "test.db"
    # 最大コネクション数
    max_connections = 3

    # 有限セマフォを生成
    sema = BoundedSemaphore(max_connections)

    # スレッドの生成
    thread_num = 5
    threads = [
        Thread(target=dbaccess, args=(dbname, sema)) for _ in range(thread_num)
    ]

    # スレッドの開始
    for thread in threads:
        thread.start()
    # 終了を待機
    for thread in threads:
        thread.join()

    logging.debug("end")


if __name__ == "__main__":
    main()
