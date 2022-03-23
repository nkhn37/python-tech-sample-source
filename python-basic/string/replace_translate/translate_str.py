"""文字列基礎
特定の文字(群)を変換/削除する translateメソッド
（変換前文字(群)と変換後文字(群)を指定する方法）

[説明ページ]
https://tech.nkhn37.net/python-replace-translate/#i-2
"""
# メソッドに直接指定する
sample_text = 'translateメソッドは,文字（群）を△変換／□削除します〇.'

print(sample_text.translate(str.maketrans(',.', '、。', '〇△□')))
