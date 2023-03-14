"""SQLiteの基本的な使い方
UPDATEでデータを更新する

[説明ページ]
https://tech.nkhn37.net/sqlite-basic/#UPDATE
"""
import sqlite3

# データベースに接続する
conn = sqlite3.connect("test.db")
# カーソルを作成する
curs = conn.cursor()

print("===== UPDATE =====")
# データを更新する
update_sql = "UPDATE person SET name=? WHERE id=?"
curs.execute(update_sql, ("SHIRO", 1))

# コミットする
conn.commit()

# カーソルとコネクションをクローズする
curs.close()
conn.close()
