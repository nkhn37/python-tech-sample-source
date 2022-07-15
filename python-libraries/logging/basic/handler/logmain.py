"""loggingモジュール
handlerの使用
logmain.pyからlogtest.pyの関数を呼び出す例

[説明ページ]
https://tech.nkhn37.net/python-logging-basic/#_handler
"""
import logging

import logtest

# ロギングの基本設定
formatter = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
logging.basicConfig(level=logging.INFO,
                    format=formatter,
                    filename='logmain.log',
                    encoding='utf_8')

logger = logging.getLogger(__name__)
logger.info('mainログ１')
logger.debug('mainログ２')

# モジュールを呼び出し
logtest.simple_func()
