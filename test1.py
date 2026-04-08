import requests
from bs4 import BeautifulSoup
import time

stock = ["1101","2330","1102"]

token = "你的 bot token"
chat_id = "你的 telegram id"

for stockid in stock:
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    # 嘗試用簡單 selector
    price_span = soup.select_one("span.Fz\\(32px\\).Fw\\(b\\)")
    if price_span:
        price = price_span.text
    else:
        price = "抓不到股價"

    message = f"股票 {stockid} 即時股價為 {price}"

    tg_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(tg_url)

    time.sleep(1)
