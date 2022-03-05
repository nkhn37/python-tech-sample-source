"""SQLAlchemyの基本的な使い方
エンジンレイヤとしての使用

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#i-2
"""
# エンジンレイヤとしてのsqlalchemyの使用
import sqlalchemy as sa

# engine = sa.create_engine('sqlite+pysqlite:///:memory:')
engine = sa.create_engine('sqlite+pysqlite:///test.db')

print('===== CREATE TABLE')
engine.execute('CREATE TABLE person ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name VARCHAR,'
               'age INTEGER)')

print('===== INSERT')
insert_sql = 'INSERT INTO person(name, age) VALUES(?, ?)'
engine.execute(insert_sql, ('TARO', 30))
engine.execute(insert_sql, ('JIRO', 20))
engine.execute(insert_sql, ('SABURO', 10))

print('===== SELECT')
rows = engine.execute('SELECT * FROM person')
print(rows)
for row in rows:
    print(row)

print('===== UPDATE')
engine.execute('UPDATE person SET name="SHIRO" WHERE id = 1')
rows = engine.execute('SELECT * FROM person')
print(rows)
for row in rows:
    print(row)

print('===== DELETE')
engine.execute('DELETE FROM person WHERE id = 2')
rows = engine.execute('SELECT * FROM person')
print(rows)
for row in rows:
    print(row)
