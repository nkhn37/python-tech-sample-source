"""multiprocessingによるマルチプロセスの基本
プロセス間におけるデータの共有
異なるサーバー間でのデータ共有: クライアント側 (キューへの登録)

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#i-6
"""
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def main():
    # オブジェクト登録
    QueueManager.register("get_queue")

    # マネージャーを取得
    manager = QueueManager(address=("localhost", 50000), authkey=b"P@ssw0rd")

    # サーバーへ接続
    manager.connect()
    queue = manager.get_queue()
    queue.put("hello")


if __name__ == "__main__":
    main()
