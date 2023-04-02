"""文字列基礎
文字列の前後から任意の文字を削除する方法
- 前後から削除する: strip
- 前から削除する: lstrip
- 後から削除する: rstrip

[説明ページ]
https://tech.nkhn37.net/python-strip-removeprefix-suffix/#i-4
"""
sample_text = "(---===![Pythonプロジェクト]!===---)"
print(f"'{sample_text}'")

# 前後から任意の文字を削除する strip
print("\n----- strip")
print(f"'{sample_text.strip('(-=![])')}'")

# 前から任意の文字を削除する lstrip
print("\n----- lstrip")
print(f"'{sample_text.lstrip('(-=![])')}'")

# 後から任意の文字を削除する rstrip
print("\n----- rstrip")
print(f"'{sample_text.rstrip('(-=![])')}'")
