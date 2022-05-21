import pandas as pd
import chromedriver_binary
from selenium import webdriver
import os
import signal
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome()
df = pd.read_csv("レビュー.csv", encoding="sjis")
df = df[["年代", "評価", "レビュー本文"]]
result = []
result2 = []
for i, row in df.iterrows():
    if row["評価"] >= 4:
        result.append(row)
    else:
        result2.append(row)
df2 = pd.DataFrame(data=result, columns=df.columns)
df3 = pd.DataFrame(data=result2, columns=df.columns)
df2.to_csv("レビュー 高評価.csv", encoding="sjis", index=False)
df3.to_csv("レビュー 低評価.csv", encoding="sjis", index=False)

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
