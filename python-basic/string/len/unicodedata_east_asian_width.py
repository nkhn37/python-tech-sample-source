"""文字列基礎
文字列の文字幅を取得する unicodedata.east_asian_width

[説明ページ]
https://tech.nkhn37.net/python-str-len-width/#unicodedataeast_asian_width
"""
import unicodedata

# 文字列の文字幅を取得する
temp_text = "Python(ﾊﾟｲｿﾝ)文字列入門２０２１年☆"
length = 0
for ch in temp_text:
    print(f"ch: {ch}, return:{unicodedata.east_asian_width(ch)}")
    # 種類によってlengthを加算する
    if unicodedata.east_asian_width(ch) in "FWA":
        length += 2
    else:
        length += 1
print(f"文字列の文字幅:{length}")
