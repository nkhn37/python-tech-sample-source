"""SQLiteの基本的な使い方
DELETEでデータを削除する

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/#DELETE
"""
import sqlite3

# データベースに接続する
conn = sqlite3.connect("test.db")
# カーソルを作成する
curs = conn.cursor()

print("===== DELETE =====")
# データを削除する
delete_sql = "DELETE FROM person WHERE id = ?"
curs.execute(delete_sql, (2,))

# コミットする
conn.commit()

# カーソルとコネクションをクローズする
curs.close()
conn.close()
