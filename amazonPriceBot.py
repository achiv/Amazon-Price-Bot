from bs4 import BeautifulSoup
import requests
import lxml

item = "https://www.amazon.com/Deep-Work-Focused-Success-Distracted/dp/0349411905/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=1609833365&sr=8-1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    }

response = requests.get(item, headers = header)
soup = BeautifulSoup(response.content, "lxml")

price = soup.select_one(selector = "#price_inside_buybox").getText()

import smtplib

title = soup.find(id="productTitle").getText().strip()

if float(price.split("$")[1]) < 16.00:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(from_addr="YOUR_EMAIL", to_addrs="YOUR_EMAIL", msg = f"Subject: Price Alert\n\n{message}\n{item}")











