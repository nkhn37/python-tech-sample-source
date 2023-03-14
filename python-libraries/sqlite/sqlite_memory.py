"""SQLiteの基本的な使い方
メモリで動作を実行させる場合

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/#i-3
"""
import sqlite3

conn = sqlite3.connect(":memory:")
curs = conn.cursor()

print("===== CREATE TABLE =====")
# テーブルを作成する
curs.execute(
    "CREATE TABLE person ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "name VARCHAR,"
    "age INTEGER)"
)
# 作成したテーブルをコミットする
conn.commit()

print("===== INSERT =====")
# プレースホルダ―を使ってデータを指定して登録する
insert_sql = "INSERT INTO person(name, age) VALUES(?, ?)"
curs.execute(insert_sql, ("TARO", 30))
curs.execute(insert_sql, ("JIRO", 20))
curs.execute(insert_sql, ("SABURO", 10))
# コミットする
conn.commit()

print("===== SELECT =====")
# データを検索する
curs.execute("SELECT * FROM person")
rows = curs.fetchall()
print(rows)

print("===== UPDATE =====")
# データを更新する
update_sql = "UPDATE person SET name=? WHERE id=?"
curs.execute(update_sql, ("SHIRO", 1))
# コミットする
conn.commit()
# データを検索する
curs.execute("SELECT * FROM person")
rows = curs.fetchall()
print(rows)

print("===== DELETE =====")
# データを削除する
curs.execute("DELETE from person WHERE id = 2")
# コミットする
conn.commit()
# データを検索する
curs.execute("SELECT * FROM person")
rows = curs.fetchall()
print(rows)

# カーソルとコネクションをクローズする
curs.close()
conn.close()
