"""loggingモジュール
ログレベルの指定方法
basicConfig関数 (level引数)

[説明ページ]
https://tech.nkhn37.net/python-logging-basic/#_level
"""
import logging

# ロギングレベルの設定(DEBUG以上を出力する)
logging.basicConfig(level=logging.DEBUG)

logging.critical('クリティカル')
logging.error('エラー')
logging.warning('ワーニング')
logging.info('インフォ')
logging.debug('デバッグ')
