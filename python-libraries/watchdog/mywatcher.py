"""Watchdogモジュール
独自の監視クラスを作成する

[説明ページ]
https://tech.nkhn37.net/python-watchdog-monitoring/#Watchdog-3
"""
import time
from argparse import ArgumentParser

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyWatchHandler(FileSystemEventHandler):
    """監視ハンドラ"""

    def __init__(self):
        """コンストラクタ"""
        super().__init__()

    def on_any_event(self, event):
        """全イベント検知

        Args:
            event: 検知イベント
        """
        # print(f'[on_any_event] {event}')
        pass

    def on_moved(self, event):
        """moved検知関数

        Args:
            event: イベント
        """
        print(f"[on_moved] {event}")

    def on_created(self, event):
        """created検知関数

        Args:
            event: イベント
        """
        print(f"[on_created] {event}")

    def on_modified(self, event):
        """modified検知関数

        Args:
            event: イベント
        """
        print(f"[on_modified] {event}")

    def on_deleted(self, event):
        """deleted検知関数

        Args:
            event: イベント
        """
        print(f"[on_deleted] {event}")


def monitor(path):
    """監視実行関数

    Args:
        path: 監視対象パス
    """
    event_handler = MyWatchHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def main():
    """メイン関数"""
    # ===== ArgumentParserの設定
    parser = ArgumentParser(description="Monitoring Tool")
    # 引数の処理
    parser.add_argument("-p", "--path", action="store", dest="path", help="監視対象パス")
    # コマンドライン引数のパース
    args = parser.parse_args()
    # 引数の取得
    path = args.path
    # pathの指定がない場合は実行ディレクトリに設定
    if path is None:
        path = "."

    # モニター実行
    monitor(path)


if __name__ == "__main__":
    main()
