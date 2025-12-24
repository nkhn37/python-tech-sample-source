"""tomllib による TOML ファイルの読み込み

[説明ページ]
https://tech.nkhn37.net/python-tomllib-basic/
"""

import tomllib

# TOMLファイルの読み込み
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

# 読み込んだデータの型を確認
print(type(config))

# 読み込んだ値の参照
print(config["WEB_SERVER"])
print(config["WEB_SERVER"]["HOST"])
print(config["WEB_SERVER"]["PORT"])

print(config["DB_SERVER"])
print(config["DB_SERVER"]["HOST"])
print(config["DB_SERVER"]["PORT"])
