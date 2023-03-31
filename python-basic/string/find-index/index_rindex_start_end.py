"""文字列基礎
index, rindexで文字列を検索する
(見つからない場合は例外(ValueError)を返却)
部分文字列を検索する場合

[説明ページ]
https://tech.nkhn37.net/python-find-rfind-index-rindex/#i-5
"""
sample_text = "Pythonプロジェクトを作ってPythonプログラミングを始めよう！"
print(sample_text)
print(sample_text[6:29])

# indexで文字列を検索する
print("--- index 部分文字列内")
try:
    print(sample_text.index("Python", 6, 29))
    print(sample_text.index("プログラミング", 6, 29))
    print(sample_text.index("JAVA", 6, 29))
except ValueError as ex:
    print(ex)

# rindexで文字列を検索する
print("--- rindex 部分文字列内")
try:
    print(sample_text.rindex("Python", 6, 29))
    print(sample_text.rindex("プログラミング", 6, 29))
    print(sample_text.rindex("JAVA", 6, 29))
except ValueError as ex:
    print(ex)
