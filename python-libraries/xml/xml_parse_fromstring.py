"""XMLモジュール
XML文字列から解析する fromstring

[説明ページ]
https://tech.nkhn37.net/python-xml-etree-elementtree/#XML-4
"""
import xml.etree.ElementTree as ET

# ファイルを読み込む
with open("./sample.xml", "r", encoding="utf-8") as f:
    xml_text = f.read()

# XML文字列を解析し、ルートを取得
root = ET.fromstring(xml_text)

# ルートノードの表示
print("===== root")
print(root)
print(root.tag)

# 子ノードを読み込む
for child1 in root:
    print("--- member infomation")
    print(f"{child1.tag}: {child1.attrib}")
    for child2 in child1:
        print(f"{child2.tag}: {child2.text}")
