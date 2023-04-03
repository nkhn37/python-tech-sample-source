"""文字列基礎
特定の文字(群)を置換/削除する translateメソッド
（辞書で置換ルールを作成する方法）

[説明ページ]
https://tech.nkhn37.net/python-replace-translate/#i-2
"""
sample_text = "translateメソッドは,文字（群）を△置換／□削除します〇."

# 置換／削除ルール辞書を作成して置換／削除する
trans_dict = {
    ",": "、",
    ".": "。",
    "〇": "",
    "△": "",
    "□": "",
}
print(sample_text.translate(str.maketrans(trans_dict)))
