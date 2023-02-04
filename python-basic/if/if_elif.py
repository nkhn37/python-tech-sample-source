"""if文基礎
elifを用いた複数の条件判定

[説明ページ]
https://tech.nkhn37.net/python-if-basic/#elif
"""
data1 = "japan"
if data1 == "japan":
    print("Japanese")
elif data1 == "USA":
    print("American")
else:
    print("Unknown")

data2 = "USA"
if data2 == "japan":
    print("Japanese")
elif data2 == "USA":
    print("American")
else:
    print("Unknown")

data3 = "China"
if data3 == "japan":
    print("Japanese")
elif data3 == "USA":
    print("American")
else:
    print("Unknown")
