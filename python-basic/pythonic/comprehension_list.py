# ===== 内包表記を使う =====
# --- 良い例 ---
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_data = [i for i in data if i % 2 == 0]
print(new_data)

# --- 悪い例 ---
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_data = []

for i in data:
    if i % 2 == 0:
        new_data.append(i)
print(new_data)
