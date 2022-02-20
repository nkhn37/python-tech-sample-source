"""入出力基礎
ファイル入出力の基本（open, write, close）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#i-2
"""
input_text = 'サンプル'

# ファイルを開く（オープン）
file = open('sample.txt', 'w+', encoding='utf-8')
# 文字列の書き込み
file.write(input_text)
# ファイルを閉じる（クローズ）
file.close()
