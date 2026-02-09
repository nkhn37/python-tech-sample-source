"""ctypes で外部 DLL を使用する方法

[説明ページ]
https://tech.nkhn37.net/python-ctypes-basic/
"""

import ctypes
from ctypes import wintypes

# user32.dllを読み込む (.dll拡張子は省略可能)
user32 = ctypes.WinDLL("user32", use_last_error=True)

# MessageBoxを定義
MessageBoxW = user32.MessageBoxW
MessageBoxW.argtypes = [
    wintypes.HWND,  # HWND (ウィンドウハンドルを示す識別子)
    wintypes.LPCWSTR,  # LPCWSTR (メッセージのテキスト)
    wintypes.LPCWSTR,  # LPCWSTR (メッセージボックスのタイトル)
    wintypes.UINT,  # UINT (メッセージボックスのスタイル)
]
MessageBoxW.restype = wintypes.INT  # 戻り値の型

# メッセージボックスを表示
result = MessageBoxW(None, "Hello, World!", "From Python", 0)

# # 以下のように無効なウィンドウハンドルでは、エラーとなる。（エラーを発生の確認例）
# result = MessageBoxW(
#     wintypes.HWND(12345678), "Hello, World!", "From Python", 0
# )

# 戻り値をチェックしてエラー処理
if result == 0:
    err = ctypes.get_last_error()
    raise ctypes.WinError(err)
else:
    print(f"MessageBox return: {result}")
