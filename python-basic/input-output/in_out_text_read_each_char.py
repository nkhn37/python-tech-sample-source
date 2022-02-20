"""入出力基礎
テキストファイルの読み込み
ファイル内容を1文字ずつ取得する（read）

[説明ページ]
https://tech.nkhn37.net/python-open-write/#1
"""
with open('sample_text.txt', 'r', encoding='utf-8') as file:
    data = []
    # 一文字ずつ読み込む
    while d := file.read(1):
        data.append(d)

print(data, '\n')
data_str = ''.join(data)
print(data_str)

# # セイウチ(Walrs)演算子を使用しない場合
# with open('sample_text.txt', 'r', encoding='utf-8') as file:
#     data = []
#     while True:
#         d = file.read(1)
#         if d == '':
#             break
#         data.append(d)
#
# print(data, '\n')
# data_str = ''.join(data)
# print(data_str)
