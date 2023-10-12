"""pandas基礎
Indexの基本
(Indexオブジェクトの集合演算)

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#Index-4
"""
import pandas as pd

indA = pd.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
indB = pd.Index([6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(f"積集合 A&B: {indA.intersection(indB)}")
print(f"和集合 A|B: {indA.union(indB)}")
print(f"差集合 A-B: {indA.difference(indB)}")
print(f"差集合 B-A: {indB.difference(indA)}")
print(f"排他的論理和 A^B: {indA.symmetric_difference(indB)}")
