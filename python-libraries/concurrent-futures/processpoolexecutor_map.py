"""concurrent.futuresを使用した並列処理
プロセスプールの使い方: ProcessPoolExecutor
mapを用いた処理

[説明ページ]

"""
import logging
import time
from concurrent.futures import ProcessPoolExecutor

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def myworker(x: int, y: int):
    logging.debug("start")

    result = x + y
    time.sleep(5)

    logging.debug(f"end: {result}")
    return result


def main():
    logging.debug("start")

    # max_workersでプロセス数を指定
    with ProcessPoolExecutor(max_workers=5) as executor:
        args = [[2, 5], [3, 10]]
        result = executor.map(myworker, *args)

        # 返却値はイテレータ
        logging.debug(result)
        # 読みだしたタイミングで実行
        logging.debug([r for r in result])

    logging.debug("end")


if __name__ == "__main__":
    main()
