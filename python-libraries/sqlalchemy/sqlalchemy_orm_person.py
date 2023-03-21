"""SQLAlchemyの基本的な使い方
オブジェクト関係マッピング（ORM）としての使用
動作確認 SQLAlchemyバージョン: 2.0.6

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#ORM
"""
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "person"

    # 属性名はテーブル名の列名に対応する
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"<Person({self.id}, {self.name}, {self.age})>"
