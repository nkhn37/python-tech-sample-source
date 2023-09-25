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
insert_sql = "INSERT INTO person(name, age) VALUES(?, ?)"
curs.execute(insert_sql, ("TARO", 30))
# コミットする
conn.commit()

# カーソルとコネクションをクローズする
curs.close()
conn.close()
