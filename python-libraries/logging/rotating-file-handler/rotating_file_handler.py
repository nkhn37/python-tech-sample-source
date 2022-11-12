"""loggingモジュール
RotaitingFileHandlerを使って指定ファイルサイズでログローテーションする方法

[説明ページ]
https://tech.nkhn37.net/python-logging-rotatingfilehandler/#RotatingFileHandler
"""
import logging.handlers
import time


def main():
    # ロギングの基本設定
    formatter = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter, encoding="utf_8")

    # ロガーの作成
    logger = logging.getLogger(__name__)

    # ログレベルをDEBUGへ変更
    logger.setLevel(logging.DEBUG)

    # ログローテーションのハンドラーを設定
    #   maxBytes: 1ログファイルの上限サイズ(byte単位)
    #   backupCount: バックアップとして保持するログファイル数
    h = logging.handlers.RotatingFileHandler("test.log", maxBytes=10000, backupCount=5)

    # フォーマットを設定
    h.setFormatter(logging.Formatter(formatter))

    # ロガーにハンドラーを設定
    logger.addHandler(h)
    
    for _ in range(1000):
        time.sleep(0.1)
        logger.debug("log rotation test")


if __name__ == "__main__":
    main()
