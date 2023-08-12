# ===== 関数へのミュータブルな引数は避ける =====
# --- 良い例 ---
def sample_function_good(in1, tmp_list=None):
    if tmp_list is None:
        tmp_list = []
    tmp_list.append(in1)
    return tmp_list


result1 = sample_function_good("A")
print(result1)
result2 = sample_function_good("B")
print(result2)


# --- 悪い例 ---
def sample_function_bad(in1, tmp_list=[]):
    tmp_list.append(in1)
    return tmp_list


result3 = sample_function_bad("A")
print(result3)
result4 = sample_function_bad("B")
print(result4)
