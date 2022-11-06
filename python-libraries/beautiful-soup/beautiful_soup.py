"""Beautiful Soupモジュール
Webスクレイピングの基本

[説明ページ]
https://tech.nkhn37.net/python-beautiful-soup-web-scraping/#Beautiful_Soup-2
"""
from bs4 import BeautifulSoup
import requests

# 対象となるURLを取得する
html = requests.get("https://www.python.org/")
# print(html.text)

# Beautiful Soupに対象のHTMLテキストを設定する
bs = BeautifulSoup(html.text, features="html.parser")

# タイトルを取得してみる
titles = bs.find_all("title")
print(titles[0].text)

# タグの内容を取得してみる
intro = bs.find_all("div", {"class": "introduction"})
print(intro[0].text)
