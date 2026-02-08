import ctypes

# user32.dllを読み込む
user32 = ctypes.WinDLL("user32.dll", use_last_error=True)
# kernel32.dllを読み込む
kernel32 = ctypes.WinDLL("kernel32.dll", use_last_error=True)


# MessageBoxを定義
MessageBox = user32.MessageBoxW
MessageBox.argtypes = [
    ctypes.c_void_p,  # HWND (ウィンドウハンドルを示す識別子)
    ctypes.c_wchar_p,  # LPCTSTR (メッセージのテキスト)
    ctypes.c_wchar_p,  # LPCTSTR (メッセージボックスのタイトル)
    ctypes.c_uint,  # UINT (メッセージボックスのスタイル)
]
MessageBox.restype = ctypes.c_int  # INT (返却値)

# GetLastErrorを定義
GetLastError = kernel32.GetLastError
GetLastError.argtypes = []
GetLastError.restype = ctypes.c_ulong

# メッセージボックスを表示
result = MessageBox(0, "Hello, World!", "From Python", 0)

# 戻り値をチェックしてエラー処理
if result == 0:
    error_code = GetLastError()
    print(f"MessageBox failed with error code: {error_code}")
else:
    print(f"MessageBox return: {result}")
