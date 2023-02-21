"""関数基礎
デコレーターを使わない高階関数による機能拡張
（デコレーターを使った実装はdecorator_basic.pyを参照）

[説明ページ]
https://tech.nkhn37.net/python-decorator/#i
"""
import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        # 処理前の時刻を設定
        timer_start = time.time()
        # 対象関数の実行
        result = func(*args, **kwargs)
        # 処理後の時刻を設定
        timer_end = time.time()
        # 処理時間を計算
        elapsed_time = timer_end - timer_start
        print(f"処理実行時間: {elapsed_time} sec")
        return result

    return wrapper


def sum_range_value(start, end, step=1):
    result = 0
    for i in range(start, end + 1, step):
        result += i
    return result


def main():
    measure_func = measure_execution_time(sum_range_value)
    sum_value = measure_func(1, 1000000)
    print(sum_value)


if __name__ == "__main__":
    main()
