"""文字列基礎
ファイルパスの組み立て (os.path.join)

※以下例は、Dドライブ直下にtestというフォルダを作成し、
任意のファイルを配置して実行することを想定して作っています。
ご使用のPCのドライブ、フォルダの状況によりパス(target_path)を
書き換えて使用してください。

[説明ページ]
https://tech.nkhn37.net/python-filepath-join/#ospathjoin
"""
import os

target_path = r"D:\test"

# 対象フォルダ内のファイル名を順に取得し、パスを作成
for f in os.listdir(target_path):
    # os.path.joinでフォルダパスとファイル名を結合
    tmp_path = os.path.join(target_path, f)
    print(tmp_path)

print("=====")
# 新しいファイル用のパスを作成
new_path = os.path.join(target_path, "tmp", "sample4.txt")
print(new_path)
