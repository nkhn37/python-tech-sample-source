import concurrent.futures
import os
import time


def io_bound_process(file_name, text):
    """IOバウンドな処理を実行する関数"""
    with open(file_name, "w+") as file:
        # ファイルに書き込み
        file.write(text)
        # シーク位置を戻して読み込み
        file.seek(0)
        file.read()

    os.remove(file_name)
    return "io_bound_process done."


def main():
    """メイン"""
    large_text = "test_string" * 10000000

    # 通常の順番でのIO処理
    start = time.time()
    print(io_bound_process("./test1.txt", large_text))
    print(io_bound_process("./test2.txt", large_text))
    end = time.time()
    print(f"順次処理 {end - start:.4f}\n")

    # マルチスレッドで処理
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        multi_thread1 = executor.submit(io_bound_process, "./test1.txt", large_text)
        multi_thread2 = executor.submit(io_bound_process, "./test2.txt", large_text)
        print(multi_thread1.result())
        print(multi_thread2.result())
        end = time.time()
        print(f"マルチスレッド {end - start:.5f}\n")

    # マルチプロセスで処理
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        multi_process1 = executor.submit(io_bound_process, "./test1.txt", large_text)
        multi_process2 = executor.submit(io_bound_process, "./test2.txt", large_text)
        print(multi_process1.result())
        print(multi_process2.result())
        end = time.time()
        print(f"CPU数: {os.cpu_count()}")
        print(f"マルチプロセス {end - start:.5f}\n")


if __name__ == "__main__":
    main()
