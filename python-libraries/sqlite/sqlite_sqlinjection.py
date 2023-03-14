"""SQLiteの基本的な使い方
プレースホルダ―を使うようにしよう (SQLインジェクション対策)

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/#i-2
"""
import sqlite3

# データベースに接続する
conn = sqlite3.connect("test.db")
# カーソルを作成する
curs = conn.cursor()

print("===== SELECT =====")
# 直接SQLを組み立てる
input_name = "SABURO"
select_sql = f"SELECT * FROM person WHERE name = '{input_name}'"
print(select_sql)
curs.execute(select_sql)
rows = curs.fetchall()
print(rows, "\n")

# 悪意ある入力の場合 (SQLインジェクション)
input_name = "SABURO' or 'A'='A"
select_sql = f"SELECT * FROM person WHERE name = '{input_name}'"
print(select_sql)
curs.execute(select_sql)
rows = curs.fetchall()
print(rows, "\n")

# プレースホルダーを使って検索する
input_name = "SABURO' or 'A'='A"
select_sql = "SELECT * FROM person WHERE name = ?"
curs.execute(select_sql, (input_name,))
rows = curs.fetchall()
print(rows)

# カーソルとコネクションをクローズする
curs.close()
conn.close()
