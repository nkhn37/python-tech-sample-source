"""loggingモジュール
フォーマットの指定方法
basicConfig関数 (format引数)

[説明ページ]
https://tech.nkhn37.net/python-logging-basic/#_format
"""
import logging

# フォーマットの設定
formatter = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
logging.basicConfig(format=formatter)

# フォーマットに従って出力される
logging.critical('クリティカル')
logging.error('エラー')
logging.warning('ワーニング')
logging.info('インフォ')
logging.debug('デバッグ')
