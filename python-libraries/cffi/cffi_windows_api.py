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
    int MessageBoxW(void *hwnd, const wchar_t *text, const wchar_t *caption, unsigned int type);
    """
)

# DLLのロード (拡張子は省略可能)
user32 = ffi.dlopen("user32")

try:
    # 変数の生成
    text = ffi.new("wchar_t[]", "Hello, World!")
    caption = ffi.new("wchar_t[]", "From Python")

    # メッセージボックスの表示 (ffi.NULL は ffi.cast("void*", 0) と同等)
    result = user32.MessageBoxW(ffi.NULL, text, caption, 0)

    # --- 以下はエラーが発生する例 ---
    # 以下のようにすると型エラーとなる
    # result = user32.MessageBoxW(ffi.NULL, 123, 456, 0)

    # 以下のように無効な HWND を指定するとWindows APIエラーとなる
    # result = user32.MessageBoxW(
    #     ffi.cast("void*", 0x12345678), text, caption, 0
    # )
    # ------------------------------------

    # 返却値が 0 の場合はエラー
    if result == 0:
        # 直前の GetLastError() の値と対応するエラーメッセージを取得
        errcode, errmsg = ffi.getwinerror()
        raise OSError(errcode, errmsg)

    print(f"MessageBox return: {result}")

except OSError as ex:
    # Windows API 呼び出しでエラーが発生した場合
    print(f"Windows API エラー: {ex}")

except TypeError as ex:
    # 引数の型が不正な場合
    print(f"引数の型エラー: {ex}")
