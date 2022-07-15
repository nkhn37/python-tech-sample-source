"""loggingモジュール
loggingモジュールの基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-logging-basic/#logging-2
"""
import logging

# デフォルトで出力されるのはWARNING以上
logging.critical('クリティカル')
logging.error('エラー')
logging.warning('ワーニング')
logging.info('インフォ')
logging.debug('デバッグ')
