"""loggingモジュール
応用：ログフィルタを適用する方法

[説明ページ]
https://tech.nkhn37.net/python-logging-config/#i-2
"""
import logging
import logging.config


class LogPwFilterSample(logging.Filter):
    """ログ出力のフィルタ例
    例）passwordというテキストが入るログメッセージは出力しない
    """
    def filter(self, record: str) -> None:
        """
        :param record: ログレコード
        :return: None
        """
        log_message = record.getMessage()
        return 'password' not in log_message


def main():
    logging.config.fileConfig('logging.ini')

    # ===== simpleExampleロガーを使用する場合
    logger_s = logging.getLogger('simpleExample')
    logger_s.addFilter(LogPwFilterSample())

    # アプリケーション内での記載方法
    logger_s.debug('デバッグメッセージ')
    logger_s.info('インフォメッセージ')
    logger_s.warning('ワーニングメッセージ')
    logger_s.error('エラーメッセージ')
    logger_s.critical('クリティカルメッセージ')
    # ログフィルタを設定しているので以下は出力されない
    logger_s.info('password = xxxxxx')


if __name__ == '__main__':
    main()
