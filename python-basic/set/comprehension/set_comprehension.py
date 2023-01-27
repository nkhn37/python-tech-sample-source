"""集合基礎
集合内包表記の使い方

[説明ページ]
https://tech.nkhn37.net/python-set-comprehension/#i-2

[内包表記まとめページ]
https://tech.nkhn37.net/python-comprehension/
"""
data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 10, 15, 20, 25, 30]

# 集合内包表記
data_set = {dt for dt in data if dt % 2 == 0}
print(f"data_set : {data_set}")
