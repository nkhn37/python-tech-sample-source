"""SQLAlchemyの基本的な使い方
SQL表現言語を用いた使用 (テーブル情報の取得方法: autoload_with)
動作確認 SQLAlchemyバージョン: 2.0.6

[説明ページ]
https://tech.nkhn37.net/python-sqlalchemy-basic/#_autoload_with
"""
import sqlalchemy as sa
from sqlalchemy import MetaData, Table

engine = sa.create_engine("sqlite+pysqlite:///test_sql.db")

# メタデータの生成
meta = MetaData()
# テーブル情報の取得
person = Table("person", meta, autoload_with=engine)

# ===== 各種person対するデータ処理を記載
# ......
