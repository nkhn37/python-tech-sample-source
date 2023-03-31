"""文字列基礎
find, rfindで文字列を検索する
(見つからない場合は-1を返却)

[説明ページ]
https://tech.nkhn37.net/python-find-rfind-index-rindex/#i-2
"""
sample_text = "Pythonプロジェクトを作ってPythonプログラミングを始めよう！"
print(sample_text)

# findで文字列を検索する
print("--- find")
print(sample_text.find("Python"))
print(sample_text.find("プログラミング"))
print(sample_text.find("JAVA"))

# rfindで文字列を検索する
print("--- rfind")
print(sample_text.rfind("Python"))
print(sample_text.rfind("プログラミング"))
print(sample_text.rfind("JAVA"))
