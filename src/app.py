import requests

request = requests.get("http://www.digikala.com/Product/DKP-21146/")

# <span id="frmLblPayablePriceAmount" class="price" itemprop="price" content="13990000.00">1,399,000</span>

print(request.content)