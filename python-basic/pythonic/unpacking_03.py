# ===== 割り当て時に値をまとめる =====
# --- 良い例 ---
data = [1, 2, 3, 4, 5]
a, *b, c = data
print(a, b, c)

# --- 悪い例 ---
data = [1, 2, 3, 4, 5]
a = data[0]
b = data[1:4]
c = data[4]
print(a, b, c)
