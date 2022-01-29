"""for文基礎
rangeで数値シーケンスを使った繰り返し処理を行う場合の注意点
（本プログラムはエラーとなる）

[注意点]
rangeはfloat型を引数に指定できない。
→ 対応する場合にはnumpyパッケージのarange関数を使用する。
  サンプルプログラムはarange_float.pyを参照

[説明ページ]
https://tech.nkhn37.net/python-for-range/#range
"""
for i in range(0.5, 5.5, 0.5):
    print(i)
