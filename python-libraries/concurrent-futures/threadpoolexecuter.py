"""concurrent.futuresを使用した並列処理
スレッドプールの使い方: ThreadPoolExecutor

[説明ページ]

"""
import logging
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")


def myworker1(x: int, y: int):
    logging.debug("start")

    result = x + y
    time.sleep(5)

    logging.debug(f"end: {result}")
    return result


def main():
    logging.debug("start")

    # max_workersでスレッド数を指定
    with ThreadPoolExecutor(max_workers=5) as executer:
        f1 = executer.submit(myworker1, 2, 3)
        f2 = executer.submit(myworker1, 5, 10)
        logging.debug(f1.result())
        logging.debug(f2.result())

    logging.debug("end")


if __name__ == "__main__":
    main()
