"""multiprocessingによるマルチプロセスの基本
プロセス間におけるデータの共有
shared ctypes: Value, Array

[説明ページ]
https://tech.nkhn37.net/python-multiprocessing-basics/#Value_Array
"""
import logging
from multiprocessing import Array, Process, Value

logging.basicConfig(level=logging.DEBUG, format="%(processName)s: %(message)s")


def myworker(num, arr):
    logging.debug("start")
    logging.debug(num)
    logging.debug(arr)

    # 値を変更
    num.value += 1.0
    for i in range(len(arr)):
        arr[i] *= 2

    # 値の表示
    logging.debug(num.value)
    logging.debug(arr[:])

    logging.debug("end")


def main():
    logging.debug("start")

    # "d":double(倍精度浮動小数) "i":sined int(符号付き整数) 他は以下を参照
    # https://docs.python.org/ja/3/library/array.html#module-array
    num = Value("d", 0.0)
    arr = Array("i", range(5))
    # 値の表示
    logging.debug(num.value)
    logging.debug(arr[:])

    # プロセスを生成
    p = Process(target=myworker, args=(num, arr))

    # プロセスの開始
    p.start()

    # プロセスの終了を待機
    p.join()

    # 値の表示
    logging.debug(num.value)
    logging.debug(arr[:])

    logging.debug("end")


if __name__ == "__main__":
    main()
