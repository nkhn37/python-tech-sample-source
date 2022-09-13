"""loggingモジュール
設定ファイル編

[説明ページ]
https://tech.nkhn37.net/python-logging-config/#logging-4
"""
import logging
import logging.config


def main():
    logging.config.fileConfig('logging.ini')

    # ===== ルートロガーを使用する場合
    logger = logging.getLogger(__name__)

    # アプリケーション内でのログ記載方法
    logger.debug('デバッグメッセージ')
    logger.info('インフォメッセージ')
    logger.warning('ワーニングメッセージ')
    logger.error('エラーメッセージ')
    logger.critical('クリティカルメッセージ')

    # ===== simpleExampleロガーを使用する場合
    logger_s = logging.getLogger('simpleExample')

    # アプリケーション内での記載方法
    logger_s.debug('デバッグメッセージ')
    logger_s.info('インフォメッセージ')
    logger_s.warning('ワーニングメッセージ')
    logger_s.error('エラーメッセージ')
    logger_s.critical('クリティカルメッセージ')


if __name__ == '__main__':
    main()
