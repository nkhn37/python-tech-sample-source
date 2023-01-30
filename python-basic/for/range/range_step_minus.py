"""for文基礎
rangeで数値シーケンスを使った繰り返し処理を行う場合
（stepでマイナス値を指定する場合）

[説明ページ]
https://tech.nkhn37.net/python-for-range/#step
"""
# stepにマイナスの数値を入れて、値が減っていく数値シーケンスを使うことも可能
for i in range(5, 0, -1):
    print(i)
