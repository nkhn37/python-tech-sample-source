"""正規表現モジュール re の使い方
オプション：複数行モードを有効にする (MULTILINE)

[説明ページ]
https://tech.nkhn37.net/python-re-options/#MULTILINE
"""
import re

text = "0123-45-6789はAさんの電話番号\n090-1111-2222はBさんの電話番号"

# マルチラインモードではない場合
ptrn1 = re.compile(r"^(\d{2,4})-(\d{2,4})-(\d{4})")

results1 = ptrn1.finditer(text)
for result1 in results1:
    print(result1.group())

print("=====")
# マルチラインモードを使用する場合
ptrn2 = re.compile(r"^(\d{2,4})-(\d{2,4})-(\d{4})", re.MULTILINE)

results2 = ptrn2.finditer(text)
for result2 in results2:
    print(result2.group())
