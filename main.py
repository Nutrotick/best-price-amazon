import requests
import smtplib
from bs4 import BeautifulSoup

# URL = "https://rozetka.com.ua/ua/sony_playstation_ps5_9709992_9812623_9837022/p319114585/"
#
# response = requests.get(url=URL)
# soup = BeautifulSoup(response.content, "html.parser")
# soup.find("p", class_="product-price__big").get_text()
# print(soup)

URL = "https://www.amazon.com/UXZDX-Microphone-Condenser-Microphones-Recording/dp/B08LZKCB3R/ref=sr_1_28?crid=15QE6I1QQXR2O&keywords=microphone&qid=1680379765&refinements=p_n_feature_ten_browse-bin%3A24677008011%7C24677010011&rnid=24676535011&s=musical-instruments&sprefix=micr%2Caps%2C205&sr=1-28"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "uk,uk-UA;q=0.9,en-US;q=0.8,en;q=0.7,ru-UA;q=0.6,ru;q=0.5",
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
price = soup.find("span", class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float > 200:
    with smtplib.SMTP("smtp.gmail.com") as sending:
        sending.starttls()
        sending.login(user=MY_EMAIL, password=MY_PASSWORD)
        sending.sendmail(from_addr=MY_EMAIL,
                         to_addrs=MY_EMAIL,
                         msg=f"Low price\n\nThe price is {price_as_float}\n{URL}")