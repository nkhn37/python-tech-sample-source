# ===== 値を交換する =====
# --- 良い例 ---
a, b = 1, 2
a, b = b, a
print(a, b)

# --- 悪い例 ---
a, b = 1, 2
tmp = a
a = b
b = tmp
print(a, b)
