"""SQLiteの基本的な使い方
SELECTでデータを検索する

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/#SELECT
"""
import sqlite3

# データベースに接続する
conn = sqlite3.connect("test.db")
# カーソルを作成する
curs = conn.cursor()

print("===== SELECT =====")
# データを検索する
select_all_sql = "SELECT * FROM person"
curs.execute(select_all_sql)
rows = curs.fetchall()
print(rows, "\n")

# 条件を指定して検索する
select_sql = "SELECT * FROM person WHERE age > ?"
curs.execute(select_sql, (20,))
rows = curs.fetchall()
print(rows)

# カーソルとコネクションをクローズする
curs.close()
conn.close()
