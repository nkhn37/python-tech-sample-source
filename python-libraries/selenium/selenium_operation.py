"""Seleniumモジュール
Webスクレイピングの基本
(画面操作)

[説明ページ]
https://tech.nkhn37.net/python-selenium-web-scraping/#Selenium-3
"""
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By

# ドライバーのパスを設定（今回は実行ファイルと同じとしてある）
CHROME_DRIVER_PATH = "chromedriver.exe"

# Webドライバーを用意する
chrome_service = service.Service(executable_path=CHROME_DRIVER_PATH)
browser = webdriver.Chrome(service=chrome_service)

# 対象のWebページを開く
browser.get("https://www.python.org/")

# ダウンロードボタンを取得する
download_button = browser.find_elements(by=By.XPATH, value='//*[@id="downloads"]/a')
# ダウンロードボタンをクリックして遷移する
download_button[0].click()
