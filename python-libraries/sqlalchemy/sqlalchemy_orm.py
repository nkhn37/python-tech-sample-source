"""SQLAlchemyの基本的な使い方
オブジェクト関係マッピング（ORM）としての使用

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#ORM
"""
# ORMとしてのsqlalchemyの使用
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = sa.create_engine('sqlite+pysqlite:///:memory:')
engine = sa.create_engine('sqlite+pysqlite:///test_orm.db')
base = declarative_base()

print('===== CREATE TABLE')
class Person(base):
    __tablename__ = 'person'
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column('name', sa.VARCHAR)
    age = sa.Column('age', sa.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'<Person({self.id}, {self.name}, {self.age})>'

base.metadata.create_all(engine)

print('===== INSERT')
# データを用意する
taro = Person(name='TARO', age=30)
jiro = Person(name='JIRO', age=20)
saburo = Person(name='SABURO', age=10)

# データベースへのセッションを作成する
Session = sessionmaker(bind=engine)
session = Session()

# セッションにデータを追加する
session.add(taro)
session.add(jiro)
session.add(saburo)
# コミットする
session.commit()

print('===== SELECT')
rows = session.query(Person.id, Person.name, Person.age).all()
for row in rows:
    print(row)
print('=== 条件を指定')
rows = session.query(Person.id, Person.name, Person.age).\
    filter(Person.age > 10).all()
for row in rows:
    print(row)

print('===== UPDATE')
p_update = session.query(Person).filter(Person.id == 1).first()
p_update.name = 'SHIRO'
session.commit()
rows = session.query(Person.id, Person.name, Person.age).all()
for row in rows:
    print(row)

print('===== DELETE')
session.query(Person).filter(Person.id == 2).delete()
session.commit()
rows = session.query(Person.id, Person.name, Person.age).all()
for row in rows:
    print(row)

# セッションをクローズする
session.close()
