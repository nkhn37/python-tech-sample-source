"""文字列基礎
特定の文字(群)を置換/削除する translateメソッド
（置換前文字（群）、置換後文字（群）、削除文字（群）を指定する方法）

[説明ページ]
https://tech.nkhn37.net/python-replace-translate/#i-3
"""
sample_text = "translateメソッドは,文字（群）を△置換／□削除します〇."

# メソッドに直接指定する
print(
    sample_text.translate(
        str.maketrans(
            ",.",
            "、。",
            "〇△□",
        )
    )
)
