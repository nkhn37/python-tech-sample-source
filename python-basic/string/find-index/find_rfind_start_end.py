"""文字列基礎
find, rfindで文字列を検索する
(見つからない場合は-1を返却)
部分文字列を検索する場合

[説明ページ]
https://tech.nkhn37.net/python-find-rfind-index-rindex/#i-3
"""
sample_text = "Pythonプロジェクトを作ってPythonプログラミングを始めよう！"
print(sample_text)
print(sample_text[6:29])

# findで部分文字列内を検索する
print("--- find 部分文字列内")
print(sample_text.find("Python", 6, 29))
print(sample_text.find("プログラミング", 6, 29))
print(sample_text.find("JAVA", 6, 29))

# rfindで文字列を検索する
print("--- rfind 部分文字列内")
print(sample_text.rfind("Python", 6, 29))
print(sample_text.rfind("プログラミング", 6, 29))
print(sample_text.rfind("JAVA", 6, 29))
