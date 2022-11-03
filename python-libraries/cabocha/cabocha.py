"""CaboChaによる構文解析の基本的な使い方
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-cabocha-syntactic-analysis/#i-2

[環境構築方法]
同フォルダのREADME.mdを参照
"""
import CaboCha

# CaboChaの構文解析器を生成する
cabocha = CaboCha.Parser()

# 解析対象の文字列を用意する
sample_text = '私はCaboChaを使ってPythonで構文解析を実装した。'

# 構文解析を実行する
result_tree = cabocha.parse(sample_text)

# 解析結果を表示する
print(result_tree.toString(CaboCha.FORMAT_TREE))
