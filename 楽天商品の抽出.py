import pandas as pd
df = pd.read_csv("astlo 商品すべて.csv", encoding="sjis")
result = []
for (_, row) in df.iterrows():
    if "香水" in str(row["商品名"]):
        result.append(row)
    # if "" in str(row["商品番号"]):
    #     result.append(row)
    # if "" in str(row["商品番号"]):
    #     result.append(row)
    # if "" in str(row["商品番号"]):
    #     result.append(row)
    # if "" in str(row["商品番号"]):
    #     result.append(row)
    # if "" in str(row["商品番号"]):
    #     result.append(row)
    # if "" in str(row["商品番号"]):
    #     result.append(row)
df2 = pd.DataFrame(data=result, columns=df.columns)
df2["コントロールカラム"] = "u"
# df2.loc[df2["商品名"].str.contains("香水"), "在庫あり時の納期"] = "2"
# df2 = df2[["コントロールカラム", "商品管理番号（商品URL）", "在庫あり時の納期"]]
# df2 = df2[df2["商品番号"].str.startswith("m")]
# df2 = df2[(df2["商品番号"].str.endswith("1") | df2["商品番号"].str.endswith("2"))]
# df2 = df2[~(df2["商品番号"].duplicated())]
# 在庫数が0のものを削除
# df2 = df2[~(df2["在庫数"] == 0)]
df2.to_csv("item.csv", encoding="sjis", index=False)
