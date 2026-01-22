"""t-string (テンプレート文字列) の基本的な使い方
t-string の構造の詳細を確認する例

[説明ページ]
https://tech.nkhn37.net/python-t-string-basic/
"""
def main():
    user = "太郎"
    age = 30
    height = 1.72

    # t-string を作成
    template = t"User={user!r}, Age next year={age + 1}, Height={height:.2f}m"

    # t-string の内容を表示
    print(f"template = {template}\n")

    # strings, interpolations, values の内容を表示
    print(f"template.strings = {template.strings}\n")

    print("template.interpolations:")
    for i, interp in enumerate(template.interpolations):
        print(f"  [{i}]")
        print(f"    value        = {interp.value!r}")
        print(f"    expression   = {interp.expression!r}")
        print(f"    conversion   = {interp.conversion!r}")
        print(f"    format_spec  = {interp.format_spec!r}\n")

    print(f"template.values = {template.values}")

if __name__ == "__main__":
    main()
