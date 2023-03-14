"""SQLiteの基本的な使い方
INSERTでデータを登録する

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/#INSERT
"""
import sqlite3

# データベースに接続する
conn = sqlite3.connect("test.db")
# カーソルを作成する
curs = conn.cursor()

print("===== INSERT =====")
# プレースホルダ―を使ってデータを指定して登録する
insert_sql = "INSERT INTO person(name, age) VALUES(?, ?)"
curs.execute(insert_sql, ("TARO", 30))
curs.execute(insert_sql, ("JIRO", 20))
curs.execute(insert_sql, ("SABURO", 10))

# コミットする
conn.commit()

# カーソルとコネクションをクローズする
curs.close()
conn.close()
