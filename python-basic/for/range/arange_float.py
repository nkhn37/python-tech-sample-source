"""for文基礎
float型の数値シーケンスで繰り返し処理を行う場合
NumPyパッケージのarangeを使用する

※ numpyパッケージがインストールされていない場合は以下のようにpipでのインストールが必要
pip install numpy

[説明ページ]
https://tech.nkhn37.net/python-for-range/#floatNumPyagange
"""
import numpy as np

for i in np.arange(0.5, 5.5, 0.5):
    print(i)
