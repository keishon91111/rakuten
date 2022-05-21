import pandas as pd

df = pd.read_csv("金額の練習.csv", encoding="sjis")
df = df[["コントロールカラム", "商品管理番号（商品URL）", "販売価格"]]
# result = []
# result2 = []
tmp = df["商品管理番号（商品URL）"].str.extract("(.*)-(\d)$")
tmp.columns = ["key", "amount"]
tmp["amount"].fillna("0", inplace=True)
print(tmp["amount"])
tmp["amount"] = tmp["amount"].astype(int)
# 増やした列を横に結合
df_new = pd.concat([df, tmp], axis=1)
# 先にkey, amountの順でソートしておく
df_new = df_new.sort_values(["key", "amount"])
# ロジックに従って計算した値で上書き
for i, row in df_new.iterrows():
    if row["amount"] > 1:
        df_new.loc[i, "販売価格"] = price * \
            row["amount"] - 50 * (row["amount"] - 1)
    else:
        price = row["販売価格"]
df = df[["コントロールカラム", "商品管理番号（商品URL）", "販売価格"]]
df_new.to_csv("金.csv", encoding="sjis", index=False)
# df_new.to_csv("金額.csv", encoding="sjis", index=False)

# for i, row in df.iterrows():
#     if row["評価"] >= 4:
#         result.append
#         df2 = pd.DataFrame(data=result, columns=df.columns)
#     else:
#         result2.appenddf3 = pd.DataFrame(data=result2, columns=df.columns)
# df2.to_csv("高評価.csv", encoding="sjis", index=False)
# df3.to_csv("低評価.csv", encoding="sjis", index=False)
