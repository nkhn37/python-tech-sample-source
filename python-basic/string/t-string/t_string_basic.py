"""t-string (テンプレート文字列) の基本的な使い方
※ Python 3.14 で追加

[説明ページ]
https://tech.nkhn37.net/python-t-string-basic/
"""
def main():
    user = "太郎"
    age = 30

    # t-string の使い方 例
    template = t"User: {user}, Age: {age}"

    # t-string の内容を表示
    print(f"template = {template}")

if __name__ == "__main__":
    main()
