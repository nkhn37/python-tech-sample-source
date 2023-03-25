"""PyYAMLによるYAMLファイル管理
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-yaml-basic/#PyYAML-2
"""
import yaml

yaml_data = {
    "WEB_SERVER": {"HOST": "192.168.1.100", "PORT": 80},
    "DB_SERVER": {"HOST": "192.168.1.200", "PORT": 3306},
}

# YAMLファイルの書き込み
with open("config.yml", "w") as yml_file:
    # 書き込み
    yaml.dump(yaml_data, yml_file)

# YAMLファイルの読み込み
with open("config.yml", "r") as yml_file1:
    # 読み込み
    load_data = yaml.load(yml_file1, Loader=yaml.SafeLoader)

print(type(load_data))
# 読み込んだ結果の参照
print(load_data["WEB_SERVER"])
print(load_data["WEB_SERVER"]["HOST"])
print(load_data["WEB_SERVER"]["PORT"])
print(load_data["DB_SERVER"])
print(load_data["DB_SERVER"]["HOST"])
print(load_data["DB_SERVER"]["PORT"])
