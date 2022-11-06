"""Seleniumモジュール
Webスクレイピングの基本
(XPathの使用)

[説明ページ]
https://tech.nkhn37.net/python-selenium-web-scraping/#XPath
"""
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

# ドライバーのパスを設定（今回は実行ファイルと同じとしてある）
CHROME_DRIVER_PATH = "./chromedriver.exe"

# Webドライバーを用意する
chrome_service = service.Service(executable_path=CHROME_DRIVER_PATH)
browser = webdriver.Chrome(service=chrome_service)

# 対象のWebページを開く
browser.get("https://www.python.org/")

# タイトルを取得してみる
print(browser.title, "\n")

# 文字列を取得してみる
elem_intro = browser.find_elements(
    by=By.XPATH, value='//*[@id="touchnav-wrapper"]/header/div/div[3]'
)
print(elem_intro[0].text)

# ブラウザを閉じる
browser.close()
