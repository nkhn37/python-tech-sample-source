def validate_age(data):
    try:
        age = int(data)
    except ValueError:
        # 入力が整数に変換できない場合
        return "入力は数字である必要があります。"
    else:
        if age < 0:
            # 年齢が負の数の場合
            return "年齢は正の数である必要があります。"
        elif age < 18:
            # 未成年の処理
            return "あなたは未成年です。"
        else:
            # 成人の処理
            return "あなたは成人です。"


print(validate_age(10))
print(validate_age(20))
print(validate_age(-10))
print(validate_age("にじゅう"))
