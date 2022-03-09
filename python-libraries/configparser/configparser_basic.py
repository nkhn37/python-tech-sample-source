"""configparserによるconfigファイル管理
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-configparser-basic/#configparserconfig-2
"""
import configparser

config = configparser.ConfigParser()
config['WEB_SERVER'] = {
    'HOST': 'xxx.xxx.xxx.xxx',
    'PORT': 80
}
config['DB_SERVER'] = {
    'HOST': 'xxx.xxx.xxx.xxx',
    'PORT': 3306
}

# configファイルへの書き込み
with open('config.ini', 'w') as config_file:
    config.write(config_file)

# configファイルからの読み込み
config1 = configparser.ConfigParser()
config1.read('config.ini')
# 読み込んだ結果を参照
print(config1['WEB_SERVER'])
print(config1['WEB_SERVER']['HOST'])
print(config1['WEB_SERVER']['PORT'])
print(config1['DB_SERVER'])
print(config1['DB_SERVER']['HOST'])
print(config1['DB_SERVER']['PORT'])
