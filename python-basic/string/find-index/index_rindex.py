"""文字列基礎
index, rindexで文字列を検索する
見つからない場合は例外(ValueError)を返却

[説明ページ]
https://tech.nkhn37.net/python-find-rfind-index-rindex/#_index_rindex
"""
sample_text = 'Pythonプロジェクトを作ってPythonプログラミングを始めよう！'

# indexで文字列を検索する
print('--- index')
try:
    print(sample_text.index('Python'))
    print(sample_text.index('プログラミング'))
    print(sample_text.index('JAVA'))
except ValueError as ex:
    print(ex)

# rindexで文字列を検索する
print('--- rindex')
try:
    print(sample_text.rindex('Python'))
    print(sample_text.rindex('プログラミング'))
    print(sample_text.rindex('JAVA'))
except ValueError as ex:
    print(ex)
