"""リスト基礎
リストの要素数をカウントする方法(countメソッド)

[説明ページ]
https://tech.nkhn37.net/python-list-count/
"""
data = ["A", "B", "A", "C", "D", "E", "A"]

# リスト内の同一要素の要素数をカウントする
cnt = data.count("A")
print(f"cnt: {cnt}")

# 見つからない場合は0を返す
cnt = data.count("Z")
print(f"cnt: {cnt}")
