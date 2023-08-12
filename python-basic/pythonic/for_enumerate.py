# ===== for文 インデックスの利用 =====
# --- 良い例 ---
data = [1, 2, 3, 4, 5]
for i, d in enumerate(data):
    print(i, d)

# --- 悪い例 ---
data = [1, 2, 3, 4, 5]
for i in range(len(data)):
    print(i, data[i])
