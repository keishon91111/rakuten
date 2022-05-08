import pandas as pd
import chromedriver_binary
from selenium import webdriver
import os
import signal
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome()
df = pd.read_csv("レビュー.csv", encoding="sjis")
result = []

for (_, row) in df.iterrows():
    if "5" in str(row["評価"]):
        result.append(row)
    if "4" in str(row["評価"]):
        result.append(row)
df2 = pd.DataFrame(data=result, columns=df.columns)
df2.drop(["商品名", "商品管理番号", "使いみち", "商品URL", "投稿日", "名前", "プロフィールURL", "件数",
         "年代", "レビューのタイトル", "使う人", "購入した回数", "評価", "性別"], axis=1, inplace=True)
df2.to_csv("レビュー　高評価.csv", encoding="sjis", index=False)
result = []
for (_, row) in df.iterrows():
    if "3" in str(row["評価"]):
        result.append(row)
    if "2" in str(row["評価"]):
        result.append(row)
    if "1" in str(row["評価"]):
        result.append(row)
df3 = pd.DataFrame(data=result, columns=df.columns)
df3.drop(["商品名", "商品管理番号", "使いみち", "商品URL", "投稿日", "名前", "プロフィールURL", "件数",
         "年代", "レビューのタイトル", "使う人", "購入した回数", "評価", "性別"], axis=1, inplace=True)
df3.to_csv("レビュー　低評価.csv", encoding="sjis", index=False)

try:
    browser.get(
        "https://auth.userlocal.jp/")
    login_path = browser.find_element_by_id("email")
    login_path.send_keys("shineproductos9111@gmail.com")
    password = browser.find_element_by_id("password")
    password.send_keys("06003713Ab")
    submit_button3 = browser.find_element_by_name("commit")
    submit_button3.click()
    element = browser.find_element_by_link_text("テキストマイニングツール")
    element.click()
    upload_button = browser.find_element_by_xpath(
        "/html/body/main/div[4]/form/ul/li[2]/label")
    upload_button.click()
    browser.find_element_by_xpath("/html/body/main/div[4]/form/div/div[1]/div[1]/div/div[3]/div[2]/input").send_keys(
        r"C:\Users\shine\Downloads\workspace\レビュー　低評価.csv")
    submit_button4 = browser.find_element_by_name("analyze")
    submit_button4.click()

finally:
    os.kill(browser.service.process.pid, signal.SIGTERM)
