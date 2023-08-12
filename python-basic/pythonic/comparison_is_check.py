# ===== Noneのチェック =====
# --- 良い例 ---
a = None
print(a is None)
print(a is not None)

# --- 悪い例 ---
a = None
print(a == None)
print(a != None)
