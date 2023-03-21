"""QtSqlのQSqlQueryModelの使い方
PostgreSQLデータベースでの使用例で使うデータの作成スクリプト

[実行前提条件]
- PostgreSQLがローカルPCにインストールされているものとする
- DB「testdb」、スキーマ「work」、ポートはデフォルトの「5432」とする
- ユーザー「test」が作成されており、パスワードは「PAssw0rd」とする
- testユーザーは、workスキーマに対して変更できる権限を設定されているものとする
  GRANT ALL ON SCHEMA work TO test;

[説明ページ]
https://tech.nkhn37.net/pyqt-qtsql-qsqlquerymodel/#PostgreSQL
"""
import psycopg2
import psycopg2.extras

host = "localhost"
port = 5432
dbname = "testdb"
user = "test"
password = "PAssw0rd"

# 接続を確立つする
con = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password,
)

# カーソルを作成する
cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)

# テーブルを作成する
print("===== CREATE TABLE work.product_info")
create_sql = (
    "CREATE TABLE work.product_info"
    "("
    "id serial NOT NULL"
    ", product_code character varying(50)"
    ", client character varying(50)"
    ", price integer"
    ", create_date_time timestamp"
    ", PRIMARY KEY (id)"
    ")"
)
cursor.execute(create_sql)
# コミット
con.commit()

# テストデータを登録する
print("===== INSERT TESTデータ")
insert_sql = (
    "INSERT INTO work.product_info "
    "(product_code, client, price, create_date_time) "
    "VALUES(%s, %s, %s, current_timestamp)"
)
cursor.execute(insert_sql, ("A", "顧客1", 1000))
cursor.execute(insert_sql, ("A", "顧客2", 2000))
cursor.execute(insert_sql, ("B", "顧客1", 1000))
cursor.execute(insert_sql, ("B", "顧客3", 4000))
cursor.execute(insert_sql, ("C", "顧客1", 2000))
# コミット
con.commit()

print("===== SELECT データ登録確認")
# データを検索する
cursor.execute("SELECT * FROM work.product_info")
rows = cursor.fetchall()
result = []
for row in rows:
    result.append(dict(row))
print(result)

# コネクションの削除
cursor.close()
con.close()
