"""loggingモジュール
TimedRotatingFileHandlerを使って指定時間でログローテーションする方法

[説明ページ]
https://tech.nkhn37.net/python-logging-timedrotatingfilehandler/#TimedRotatingFileHandler
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
    #   when: intervalの単位
    #         ('S':秒、'M':分、'H':時間、'D':日、'W0'-'W6':曜日(0=月曜))
    #   interval: ログローテーション間隔
    #   backupCount: バックアップとして保持するログファイル数
    h = logging.handlers.TimedRotatingFileHandler(
        "test.log", when="S", interval=20, backupCount=5
    )

    # フォーマットを設定
    h.setFormatter(logging.Formatter(formatter))

    # ロガーにハンドラーを設定
    logger.addHandler(h)

    for _ in range(1000):
        time.sleep(0.1)
        logger.debug("log rotation test")


if __name__ == "__main__":
    main()
