# ===== 複数の変数に値を割り当てる =====
# --- 良い例 ---
data = [1, 2, 3, 4, 5]
a, b, c, d, e = data
print(a, b, c, d, e)

# --- 悪い例 ---
data = [1, 2, 3, 4, 5]
a = data[0]
b = data[1]
c = data[2]
d = data[3]
e = data[4]
print(a, b, c, d, e)
