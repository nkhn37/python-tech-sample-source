"""文字列基礎
日本語（マルチバイト文字）の文字列の文字幅を取得する east_asian_width関数
unicodedataモジュールをインポートして使用する

[説明ページ]
https://tech.nkhn37.net/python-len-east_asian_width/
"""
# 日本語（マルチバイト文字）の幅で長さを取得する
import unicodedata

temp_text = 'Python(ﾊﾟｲｿﾝ)文字列入門２０２１年☆'
length = 0
for ch in temp_text:
    print(f'ch: {ch}, return:{unicodedata.east_asian_width(ch)}')
    if unicodedata.east_asian_width(ch) in 'FWA':
        length += 2
    else:
        length += 1
print(f'文字列の長さは:{length}')
