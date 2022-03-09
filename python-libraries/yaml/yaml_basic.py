"""PyYAMLによるYAMLファイル管理
基本的な使い方

[説明ページ]
https://tech.nkhn37.net/python-yaml-basic/#PyYAMLYAML
"""
import yaml

with open('config.yml', 'w') as yml_file:
    dump_data = {
        'WEB_SERVER': {
            'HOST': 'xxx.xxx.xxx.xxx',
            'PORT': 80
        },
        'DB_SERVER': {
            'HOST': 'xxx.xxx.xxx.xxx',
            'PORT': 3306
        }
    }

    # yamlファイルへの書き込み
    yaml.dump(dump_data, yml_file)

# yamlファイルからの読み込み
with open('config.yml', 'r') as yml_file1:
    data = yaml.load(yml_file1, Loader=yaml.SafeLoader)
    # 読み込んだ結果の参照
    print(type(data))
    print(data)
    print('=====')
    print(data['WEB_SERVER'])
    print(data['WEB_SERVER']['HOST'])
    print(data['WEB_SERVER']['PORT'])
    print('=====')
    print(data['DB_SERVER'])
    print(data['DB_SERVER']['HOST'])
    print(data['DB_SERVER']['PORT'])
