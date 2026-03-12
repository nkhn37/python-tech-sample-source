import concurrent.futures
import os
import time


def cpu_bound_process():
    """CPUバウンドな処理を実行する関数"""
    i = 0
    while i < 100000000:
        i = i + 1
    return "cpu_bound_process done."


def main():
    """メイン"""
    # 通常の順番でのCPU処理
    start = time.time()
    print(cpu_bound_process())
    print(cpu_bound_process())
    end = time.time()
    print(f"順次処理 {end - start:.4f}\n")

    # マルチスレッドで処理
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        start = time.time()
        multi_thread1 = executor.submit(cpu_bound_process)
        multi_thread2 = executor.submit(cpu_bound_process)
        print(multi_thread1.result())
        print(multi_thread2.result())
        end = time.time()
        print(f"マルチスレッド {end - start:.5f}\n")

    # マルチプロセスで処理
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        start = time.time()
        multi_process1 = executor.submit(cpu_bound_process)
        multi_process2 = executor.submit(cpu_bound_process)
        print(multi_process1.result())
        print(multi_process2.result())
        end = time.time()
        print(f"CPU数: {os.cpu_count()}")
        print(f"マルチプロセス {end - start:.5f}\n")


if __name__ == "__main__":
    main()
