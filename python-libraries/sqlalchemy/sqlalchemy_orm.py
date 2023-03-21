"""SQLAlchemyの基本的な使い方
オブジェクト関係マッピング（ORM）としての使用

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#ORM
"""
import sqlalchemy as sa
import sqlalchemy_orm_person
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from sqlalchemy_orm_person import Person

# engine = sa.create_engine("sqlite+pysqlite:///test_orm.db")
# engine = sa.create_engine("sqlite+pysqlite:///test_orm.db", echo=True)
engine = sa.create_engine("sqlite+pysqlite:///:memory:")

print("===== CREATE TABLE =====")
sqlalchemy_orm_person.Base.metadata.create_all(engine)

print("\n===== INSERT =====")
with Session(engine) as session:
    taro = Person(name="TARO", age=30)
    jiro = Person(name="JIRO", age=20)
    saburo = Person(name="SABURO", age=10)

    session.add_all([taro, jiro, saburo])
    session.commit()

print("\n===== SELECT =====")
with Session(engine) as session:
    select_all_sql = select(Person)
    rows = session.scalars(select_all_sql)
    for row in rows:
        print(row)
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 条件で検索する場合
print("=== 条件指定")
with Session(engine) as session:
    select_sql = select(Person).where(Person.age > 20)
    rows = session.scalars(select_sql)
    for row in rows:
        print(row)
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

print("\n===== UPDATE =====")
with Session(engine) as session:
    # 主キーを指定して取得する
    target_person = session.get(Person, 1)
    # # 以下でも同様
    # select_sql = select(Person).where(Person.id == 1)
    # target_person = session.scalars(select_sql).one()
    target_person.name = "SHIRO"
    target_person.age = 40
    session.commit()

    # 更新後の結果を確認
    select_all_sql = select(Person)
    rows = session.scalars(select_all_sql)
    for row in rows:
        print(row)
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 複数行更新する場合
print("=== 複数行を更新")
with Session(engine) as session:
    update_sql = update(Person)
    update_data = [
        {"id": 2, "name": "GORO", "age": 50},
        {"id": 3, "name": "ROKURO", "age": 60},
    ]
    session.execute(update_sql, update_data)
    session.commit()

    # 更新後の結果を確認
    select_all_sql = select(Person)
    rows = session.scalars(select_all_sql)
    for row in rows:
        print(row)
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

print("\n===== DELETE =====")
with Session(engine) as session:
    # 主キーを指定して取得する
    target_person = session.get(Person, 1)
    # # 以下でも同様
    # select_sql = select(Person).where(Person.id == 1)
    # target_person = session.scalars(select_sql).one()

    # データを削除する
    session.delete(target_person)
    session.commit()

    # 削除後の結果を確認
    select_all_sql = select(Person)
    rows = session.scalars(select_all_sql)
    for row in rows:
        print(row)
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")

# 複数行削除する場合
print("=== 複数行を削除")
with Session(engine) as session:
    delete_sql = delete(Person).where(Person.id.in_([2, 3]))
    session.execute(delete_sql)
    session.commit()

    # 更新後の結果を確認
    select_all_sql = select(Person)
    rows = session.scalars(select_all_sql)
    for row in rows:
        print(row)
        print(f"id:{row.id}, name: {row.name}, age: {row.age}")
