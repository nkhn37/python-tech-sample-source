"""SQLiteの基本的な使い方

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/
"""
import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('test.db')
curs = conn.cursor()

print('===== CREATE TABLE')
# テーブルを作成する
curs.execute('CREATE TABLE person ('
             'id INTEGER PRIMARY KEY AUTOINCREMENT, '
             'name VARCHAR,'
             'age INTEGER)')
# 作成したテーブルをコミットする
conn.commit()

print('===== INSERT')
# データを追加する
curs.execute('INSERT INTO person(name, age) VALUES("TARO", 30)')
curs.execute('INSERT INTO person(name, age) VALUES("JIRO", 20)')
# プレースホルダーを使ってデータを追加する
insert_sql = 'INSERT INTO person(name, age) VALUES(?, ?)'
curs.execute(insert_sql, ("SABURO", 10))
# コミットする
conn.commit()

print('===== SELECT')
# データを検索する
curs.execute('SELECT * FROM person')
rows = curs.fetchall()
print(rows)

print('===== UPDATE')
# データを更新する
curs.execute('UPDATE person SET name="SHIRO" WHERE id = 1')
conn.commit()
curs.execute('SELECT * FROM person')
rows = curs.fetchall()
print(rows)

print('===== DELETE')
# データを削除する
curs.execute('DELETE from person WHERE id = 2')
conn.commit()
curs.execute('SELECT * FROM person')
rows = curs.fetchall()
print(rows)

# カーソルとコネクションをクローズする
curs.close()
conn.close()
