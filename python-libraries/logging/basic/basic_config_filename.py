"""loggingモジュール
ログをファイルに出力する方法
basicConfig関数 (filename引数)

[説明ページ]
https://tech.nkhn37.net/python-logging-basic/#_filename
"""
import logging

# ファイルにログ情報を出力する
logging.basicConfig(filename='test.log', encoding='utf_8')

logging.critical('クリティカル')
logging.error('エラー')
logging.warning('ワーニング')
logging.info('インフォ')
logging.debug('デバッグ')
