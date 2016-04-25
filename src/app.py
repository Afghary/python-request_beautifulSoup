import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.digikala.com/Product/DKP-21146/")
content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("span",attrs={"id":"frmLblPayablePriceAmount","class":"price","itemprop":"price"})
stringPrice = element.text.strip()

priceWithoutComma = stringPrice.replace(",","")
price = int(priceWithoutComma)

if price < 1000000:
    print("You shuold buy it!")
else:
    print("Don't buy it, it's too expensive.")
    print("Current price is: {} Rials".format(price))

# <span id="frmLblPayablePriceAmount" class="price" itemprop="price" content="13990000.00">1,399,000</span>

#print(request.content)