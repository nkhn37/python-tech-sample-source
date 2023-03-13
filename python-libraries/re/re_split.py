"""正規表現モジュール re の使い方
splitメソッドを用いた文字列の分割
（正規表現で一致した部分を基準に文字列を分割する）

[説明ページ]
https://tech.nkhn37.net/python-re-split-sub/#split
"""
import re

text = (
    "私の電話は0123-45-6789で、携帯は090-1111-2222です。"
    "Aさんの電話は9876-54-3210で、携帯は080-3333-4444です。"
)

# パターンを設定
ptrn1 = re.compile(r"\d{2,4}-\d{2,4}-\d{4}")

# 正規表現で一致した位置を基準に文字列を分割する
split_result = ptrn1.split(text)
print(split_result)
