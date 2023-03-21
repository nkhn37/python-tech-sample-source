"""SQLAlchemyの基本的な使い方
SQL表現言語を用いた使用
動作確認 SQLAlchemyバージョン: 2.0.6

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#SQL
"""
import sqlalchemy as sa
from sqlalchemy import Column, Integer, MetaData, String, Table, bindparam

# engine = sa.create_engine("sqlite+pysqlite:///test_sql.db")
# engine = sa.create_engine("sqlite+pysqlite:///test_sql.db", echo=True)
engine = sa.create_engine("sqlite+pysqlite:///:memory:")

# メタデータの生成
meta = MetaData()

print("===== CREATE TABLE =====")
person = Table(
    "person",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("age", Integer),
)
meta.create_all(engine)

print("\n===== INSERT =====")
# 1行挿入する場合
with engine.connect() as conn:
    insert_sql = person.insert().values(name="TARO", age=30)
    result = conn.execute(insert_sql)
    conn.commit()
    print(f"挿入件数: {result.rowcount}")

# 複数行挿入する場合
with engine.connect() as conn:
    insert_sql = person.insert()
    input_data = [
        {"name": "JIRO", "age": 20},
        {"name": "SABURO", "age": 10},
    ]
    result = conn.execute(insert_sql, input_data)
    conn.commit()
    print(f"挿入件数: {result.rowcount}")

print("\n===== SELECT =====")
# 全て検索する場合
with engine.connect() as conn:
    select_all_sql = person.select()
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 条件で検索する場合
print("=== 条件指定")
with engine.connect() as conn:
    select_sql = person.select().where(person.c.age > 20)
    rows = conn.execute(select_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

print("\n===== UPDATE =====")
with engine.connect() as conn:
    update_sql = (
        person.update().where(person.c.id == 1).values(name="SHIRO", age=40)
    )
    result = conn.execute(update_sql)
    conn.commit()
    print(f"更新行数: {result.rowcount}")

    # 更新後の結果を確認
    select_all_sql = person.select()
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 複数行更新する場合
print("=== 複数行を更新")
with engine.connect() as conn:
    update_sql = (
        person.update()
        .where(person.c.id == bindparam("old_id"))
        .values(name=bindparam("new_name"), age=bindparam("new_age"))
    )
    update_data = [
        {"old_id": 2, "new_name": "GORO", "new_age": 50},
        {"old_id": 3, "new_name": "ROKURO", "new_age": 60},
    ]
    result = conn.execute(update_sql, update_data)
    conn.commit()
    print(f"更新行数: {result.rowcount}")

    # 更新後の結果を確認
    select_all_sql = person.select()
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

print("\n===== DELETE =====")
with engine.connect() as conn:
    delete_sql = person.delete().where(person.c.id == 1)
    result = conn.execute(delete_sql)
    conn.commit()
    print(f"削除件数: {result.rowcount}")

    # 削除後の結果を確認
    select_all_sql = person.select()
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 複数行を削除する場合
print("=== 複数行を削除")
with engine.connect() as conn:
    delete_sql = person.delete().where(person.c.id == bindparam("delete_id"))
    delete_data = [
        {"delete_id": 2},
        {"delete_id": 3},
    ]
    result = conn.execute(delete_sql, delete_data)
    conn.commit()
    print(f"削除件数: {result.rowcount}")

    # 削除後の結果を確認
    select_all_sql = person.select()
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")
