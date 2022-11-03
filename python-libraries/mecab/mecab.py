"""Mecabによる形態素解析
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-mecab-morphological-analysis/#PythonMeCab-2

[MeCabの環境準備方法]
https://tech.nkhn37.net/python-mecab-morphological-analysis/#i-2
"""
import MeCab

# MeCabの解析気を用意する
# Taggerのinitでunidicの読み込みがされる
tagger = MeCab.Tagger()

# 解析対象の文字列を用意する
sample_text = 'Pythonで形態素解析をしてみます。'

# 形態素解析を実行する
result = tagger.parse(sample_text)

# 形態素解析結果を表示する
print(result)
