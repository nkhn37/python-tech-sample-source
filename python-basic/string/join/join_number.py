"""文字列基礎
リストを結合して文字列にする方法 join
数値リストの結合（エラー対応版）

[説明ページ]
https://tech.nkhn37.net/python-str-join/#i-2
"""
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 数値リストをjoinで結合する場合はリスト内包表記でstrに変換してからjoinに渡す
print(','.join([str(i) for i in sample_list]))
