"""入出力基礎
ファイル入出力の基本（with命令により自動でファイルをクローズする）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#withclose
"""
input_text = 'サンプル'

# with命令でopenを実行する
with open('sample.txt', 'w+', encoding='utf-8') as file:
    # 文字列の書き込み
    file.write(input_text)
