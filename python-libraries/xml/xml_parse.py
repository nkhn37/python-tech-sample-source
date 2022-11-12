"""XMLモジュール
XMLファイルから直接読み込み解析する parse

[説明ページ]
https://tech.nkhn37.net/python-xml-etree-elementtree/#XML-3
"""
import xml.etree.ElementTree as ET

# XMLファイルを解析する
xml_tree = ET.parse("./sample.xml")

# ルートを取得
root = xml_tree.getroot()

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
