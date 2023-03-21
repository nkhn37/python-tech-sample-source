"""QtSqlのQSqlQueryModelの使い方
SQLiteデータベースでの使用例で使うデータの作成スクリプト

[説明ページ]
https://tech.nkhn37.net/pyqt-qtsql-qsqlquerymodel/#SQLite
"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect("test.db")
curs = conn.cursor()

print("===== CREATE TABLE")
# テーブルを作成する
curs.execute(
    "CREATE TABLE product_info ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT"
    ", product_code VARCHAR"
    ", client VARCHAR"
    ", price INTEGER"
    ", create_date_time TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')))"
)
# 作成したテーブルをコミットする
conn.commit()

print("===== INSERT")
insert_sql = (
    "INSERT INTO product_info(product_code, client, price) VALUES(?, ?, ?)"
)
curs.execute(insert_sql, ("A", "顧客1", 1000))
curs.execute(insert_sql, ("A", "顧客2", 2000))
curs.execute(insert_sql, ("B", "顧客1", 1000))
curs.execute(insert_sql, ("B", "顧客3", 4000))
curs.execute(insert_sql, ("C", "顧客1", 2000))
# コミットする
conn.commit()

print("===== SELECT")
# データを検索する
curs.execute("SELECT * FROM product_info")
rows = curs.fetchall()
print(rows)

# カーソルとコネクションをクローズする
curs.close()
conn.close()
