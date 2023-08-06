"""クラス基礎
コンテキストマネージャーの基本
（with...as命令にオブジェクトを渡す方法）

[説明ページ]
https://tech.nkhn37.net/python-context-manager-basic/
"""


class SampleContext:
    # コンテキストを作成する
    def __enter__(self):
        print("--- コンテキスト開始(enter) ---")
        return self

    # コンテキストを終了する
    def __exit__(self, exception_type, exception_value, traceback):
        print("--- コンテキスト終了(exit) ---")
        if exception_type is None:
            print("エラーなし")
        else:
            print(f"エラー: {exception_type}, {exception_value}, {traceback}")
            return True

    # 任意の関数
    @staticmethod
    def test():
        print("testメソッド")


def main():
    with SampleContext() as sample:
        sample.test()
        # # 何かしらエラーが発生すると挙動が変わる
        # raise ValueError("不正な値")

    print("後続処理")


if __name__ == "__main__":
    main()
