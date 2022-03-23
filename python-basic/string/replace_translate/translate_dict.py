"""文字列基礎
特定の文字(群)を変換/削除する translateメソッド
（辞書で変換ルールを作成する方法）

[説明ページ]
https://tech.nkhn37.net/python-replace-translate/#i
"""
# 変換／削除ルール辞書を作成して変換／削除する
sample_text = 'translateメソッドは,文字（群）を△変換／□削除します〇.'

trans_dict = {
    ',': '、',
    '.': '。',
    '〇': '',
    '△': '',
    '□': ''
}

print(sample_text.translate(str.maketrans(trans_dict)))
