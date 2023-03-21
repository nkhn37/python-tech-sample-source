"""SQLAlchemyの基本的な使い方
エンジンレイヤとしての使用
動作確認 SQLAlchemyバージョン: 2.0.6

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#i-2
"""
import sqlalchemy as sa
from sqlalchemy import text

# engine = sa.create_engine("sqlite+pysqlite:///test_engine.db")
# engine = sa.create_engine("sqlite+pysqlite:///test_engine.db", echo=True)
engine = sa.create_engine("sqlite+pysqlite:///:memory:")

print("===== CREATE TABLE =====")
with engine.connect() as conn:
    create_table_sql = text(
        "CREATE TABLE IF NOT EXISTS person ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT"
        ",name VARCHAR"
        ",age INTEGER)"
    )
    conn.execute(create_table_sql)
    conn.commit()

print("\n==== INSERT =====")
with engine.connect() as conn:
    insert_sql = text("INSERT INTO person(name, age) VALUES(:name, :age)")
    result = conn.execute(insert_sql, {"name": "TARO", "age": 30})
    conn.commit()
    print(f"挿入件数: {result.rowcount}")

with engine.connect() as conn:
    insert_sql = text("INSERT INTO person(name, age) VALUES(:name, :age)")
    input_data = [
        {"name": "JIRO", "age": 20},
        {"name": "SABURO", "age": 10},
    ]
    result = conn.execute(insert_sql, input_data)
    conn.commit()
    print(f"挿入件数: {result.rowcount}")

print("\n===== SELECT =====")
with engine.connect() as conn:
    select_all_sql = text("SELECT * FROM person")
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 条件を指定する場合
print("=== 条件指定")
with engine.connect() as conn:
    select_sql = text("SELECT * FROM person WHERE age > :age")
    rows = conn.execute(select_sql, {"age": 20})
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

print("\n===== UPDATE =====")
with engine.connect() as conn:
    update_sql = text("UPDATE person SET name=:name, age=:age WHERE id = :id")
    result = conn.execute(update_sql, {"name": "SHIRO", "age": 40, "id": 1})
    conn.commit()
    print(f"更新行数: {result.rowcount}")

    # 更新後の結果表示
    select_all_sql = text("SELECT * FROM person")
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 複数行更新する場合
print("=== 複数行を更新")
with engine.connect() as conn:
    update_sql = text("UPDATE person SET name=:name, age=:age WHERE id = :id")
    update_data = [
        {"name": "GORO", "age": 50, "id": 2},
        {"name": "ROKURO", "age": 60, "id": 3},
    ]
    result = conn.execute(update_sql, update_data)
    conn.commit()
    print(f"更新行数: {result.rowcount}")

    # 更新後の結果表示
    select_all_sql = text("SELECT * FROM person")
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

print("\n===== DELETE =====")
with engine.connect() as conn:
    delete_sql = text("DELETE FROM person WHERE id = :id")
    result = conn.execute(delete_sql, {"id": 1})
    conn.commit()
    print(f"削除件数: {result.rowcount}")

    # 削除後の結果表示
    select_all_sql = text("SELECT * FROM person")
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 複数行を削除する場合
print("=== 複数行を削除")
with engine.connect() as conn:
    delete_sql = text("DELETE FROM person WHERE id = :id")
    delete_data = [
        {"id": 2},
        {"id": 3},
    ]
    result = conn.execute(delete_sql, delete_data)
    conn.commit()
    print(f"削除件数: {result.rowcount}")

    # 削除後の結果表示
    select_all_sql = text("SELECT * FROM person")
    rows = conn.execute(select_all_sql)
    for row in rows:
        print(row, type(row))
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")
