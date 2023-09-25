"""threadingによるマルチスレッド処理の基本
通常のSemaphoreは値が初期値を超えても問題なし

[説明ページ]
https://tech.nkhn37.net/python-threading-multithread/#_BoundedSemaphore
"""
from threading import Semaphore

# 最大数(初期値)
max_sema = 2

# セマフォを生成
sema = Semaphore(max_sema)
# 初期値 value=2
print(sema)

# value=1
sema.acquire()
print(sema)
# value=0
sema.acquire()
print(sema)

# value=1
sema.release()
print(sema)
# value=2
sema.release()
print(sema)
# value=3 ← 初期値の最大を超える
sema.release()
print(sema)
