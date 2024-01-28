"""pandasの基礎
PeriodIndexの作成
特定の期間を表すインデックスに適している（例：月単位や四半期単位）

[説明ページ]
https://tech.nkhn37.net/pandas-index-basic/#PeriodIndex
"""
import pandas as pd

# 月単位のPeriodIndexを作成
monthly_period = pd.period_range(
    start="2024-01",
    end="2024-12",
    freq="M",
)
print(monthly_period, "\n")

# データフレームの作成
df_period = pd.DataFrame(
    data=list(range(1, 13)),
    index=monthly_period,
    columns=["data"],
)
print(df_period)
