"""SQLAlchemyの基本的な使い方
SQL表現言語を用いた使用

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#SQL
"""
# SQL表現言語としてのsqlalchemyの使用
import sqlalchemy as sa

# engine = sa.create_engine('sqlite+pysqlite:///:memory:')
engine = sa.create_engine('sqlite+pysqlite:///test_sql.db')

print('===== CREATE TABLE')
meta = sa.MetaData()
person = sa.Table('person', meta,
                  sa.Column('id', sa.Integer,
                            primary_key=True, autoincrement=True),
                  sa.Column('name', sa.VARCHAR),
                  sa.Column('age', sa.Integer))
meta.create_all(engine)

print('===== INSERT')
engine.execute(person.insert({'name': 'TARO', 'age': 30}))
engine.execute(person.insert({'name': 'JIRO', 'age': 20}))
engine.execute(person.insert({'name': 'SABURO', 'age': 10}))

print('===== SELECT')
rows = engine.execute(person.select())
print(rows)
for row in rows:
    print(row)
print('== 条件を指定　age > 10')
rows = engine.execute(person.select().where(person.c.age > 10))
print(rows)
for row in rows:
    print(row)

print('===== UPDATE')
engine.execute(person.update().where(person.c.id == 1).values(name='SHIRO'))
rows = engine.execute(person.select())
print(rows)
for row in rows:
    print(row)

print('===== DELETE')
engine.execute(person.delete().where(person.c.id == 2))
rows = engine.execute(person.select())
print(rows)
for row in rows:
    print(row)
