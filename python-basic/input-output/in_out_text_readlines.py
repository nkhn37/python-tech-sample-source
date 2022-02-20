"""入出力基礎
テキストファイルの読み込み
ファイル内容を1行ずつ取得する（readlines）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#1-2
"""
with open('sample_text.txt', 'r', encoding='utf-8') as file:
    # 1行ずつデータを読み出す
    data = file.readlines()

print(data, '\n')
# 取得したデータを出力
for line in data:
    print(line, end='')

# # for文で順次取り出す方法
# with open('sample_text.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')
