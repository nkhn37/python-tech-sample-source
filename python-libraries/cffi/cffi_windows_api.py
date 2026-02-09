"""CFFI で外部 DLL を使用する方法

[説明ページ]
https://tech.nkhn37.net/python-cffi-basic/
"""

from cffi import FFI

# FFIインスタンスの生成
ffi = FFI()

# 関数の宣言
ffi.cdef(
    """
    // メッセージボックス
    int MessageBoxW(void *hwnd, const wchar_t *text, const wchar_t *caption, unsigned int type);
"""
)

# DLLのロード
user32 = ffi.dlopen("user32.dll")

try:
    # MessageBoxの表示
    result = user32.MessageBoxW(ffi.NULL, "Hello, World!", "From Python", 0)
    print(f"MessageBox return: {result}")

except TypeError as ex:
    print(f"An error occurred: {ex}")
