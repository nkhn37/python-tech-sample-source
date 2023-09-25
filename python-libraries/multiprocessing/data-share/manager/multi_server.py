"""multiprocessingによるマルチプロセスの基本
プロセス間におけるデータの共有
異なるサーバー間でのデータ共有: サーバー側

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#i-6
"""
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def main():
    q = queue.Queue()

    # マネージャーで呼び出し可能なオブジェクト登録
    QueueManager.register("get_queue", callable=lambda: q)

    # マネージャーを取得
    # address: マネージャープロセスが新たなコネクションを待ち受けるアドレス
    # authkey: サーバープロセスへのコネクションを検証するための認証キー
    manager = QueueManager(address=("localhost", 50000), authkey=b"P@ssw0rd")

    # サーバーを取得
    server = manager.get_server()
    # サーバーを起動する
    server.serve_forever()


if __name__ == "__main__":
    main()
