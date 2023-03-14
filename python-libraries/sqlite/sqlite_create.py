"""SQLiteの基本的な使い方
CREATE TABLEでテーブルを作成する

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/#CREATE_TABLE
"""
import sqlite3

# データベースに接続する
conn = sqlite3.connect("test.db")
# カーソルを作成する
curs = conn.cursor()

print("===== CREATE TABLE =====")
# テーブルを作成する
curs.execute(
    "CREATE TABLE IF NOT EXISTS person ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT"
    ",name VARCHAR"
    ",age INTEGER)"
)
# コミットする
conn.commit()

# カーソルとコネクションをクローズする
curs.close()
conn.close()
