# ===== for文 複数のシーケンスをまとめて処理 =====
# --- 良い例 ---
data1 = [1, 2, 3, 4, 5]
data2 = "abcde"
for d1, d2 in zip(data1, data2):
    print(d1, d2)

# --- 良い例 ---
data1 = [1, 2, 3, 4, 5]
data2 = "abcde"
for d in zip(data1, data2):
    print(d)

# --- 悪い例 ---
data1 = [1, 2, 3, 4, 5]
data2 = "abcde"
for i in range(len(data1)):
    print(data1[i], data2[i])
