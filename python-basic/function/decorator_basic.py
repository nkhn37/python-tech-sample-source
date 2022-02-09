"""関数基礎
デコレータの基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-decorator/#i-2
"""
import time
from functools import wraps


def measure_execution_time(func):
    """ 時間計測デコレータ用関数
    :param func: 対象関数
    :return: wrapper関数
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """内部ラッパー関数
        """
        # 処理前の時刻を設定
        timer_start = time.time()
        # 対象関数の実行
        result = func(*args, **kwargs)
        # 処理後の時刻を設定
        timer_end = time.time()
        # 処理時間を計算
        elapsed_time = timer_end - timer_start
        print(f'処理実行時間: {elapsed_time} sec')
        return result

    return wrapper


@measure_execution_time
def sum_range_value(start, end, step=1):
    """範囲内の数値を合計する関数
    :param start: 開始数値
    :param end: 終了数値
    :param step: ステップ値
    :return: 合計結果
    """
    result = 0
    for i in range(start, end+1, step):
        result += i
    return result


def main():
    sum_value = sum_range_value(1, 1000000)
    print(sum_value)
    print(f'\ndocstring:\n{sum_range_value.__doc__}')


if __name__ == '__main__':
    main()
