"""loggingモジュール
loggerの使用
logmain.pyからlogtest.pyの関数を呼び出す例

[説明ページ]
https://tech.nkhn37.net/python-logging-basic/#_logger
"""
import logging

# モジュール用のロガーを設定 DEBUGに設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def simple_func():
    logger.info('logtestログ１')
    logger.debug('logtestログ２')


def main():
    pass


if __name__ == '__main__':
    main()
