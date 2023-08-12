# ===== with..as命令を使ってリソースを適切に開放する =====
# --- 良い例 ---
with open("temp_file.txt", "w", encoding="utf-8") as f:
    f.write("test")

# --- 悪い例 ---
tmp_file = open("temp_file.txt", "w", encoding="utf-8")
tmp_file.write("test")
tmp_file.close()
