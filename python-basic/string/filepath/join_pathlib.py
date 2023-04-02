"""文字列基礎
ファイルパスの組み立て (pathlibの使用)

※以下例は、Dドライブ直下にtestというフォルダを作成し、
任意のファイルを配置して実行することを想定して作っています。
ご使用のPCのドライブ、フォルダの状況によりパスを書き換えて使用してください。

[説明ページ]
https://tech.nkhn37.net/python-filepath-join/#pathlibjoinpath
"""
import pathlib

target_path = r"D:\test"

# Pathオブジェクトを作成
path = pathlib.Path(r"D:\test")

# 対象フォルダ内のファイルを取得
file_path = [x for x in path.iterdir() if x.is_file()]
print(file_path)
# 色々なメソッドを使用することが可能
print(file_path[0].is_file())
print(file_path[0].is_dir())
print(file_path[0].drive)
print(file_path[0].name)

print("=====")
# 新しいファイル用のパスを作成
new_path = path.joinpath("tmp", "sample4.txt")
print(new_path)
print(type(new_path))
