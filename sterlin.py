#Bu program bankaların güncel İngiliz Sterlini alış ve satış fiyatlarını grafiğe döker.
#This program charts Turkish banks' current GBP/TRY buying and selling prices.

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd


r = requests.get("https://kur.doviz.com/serbest-piyasa/sterlin")

soup = BeautifulSoup(r.text, "xml")

table = soup.find("div", class_="table")

td = table.find_all("td")

i = 0
banka=[]
alis = []
satis = []
for i in range(0,len(td),3):
  banka.append(td[i].text)
  alis.append(float((td[i+1].text).replace(',', '.')))
  satis.append(float((td[i+2].text).replace(',', '.')))

d = {'Banka': banka, 'Alış': alis, 'Satış': satis}
df = pd.DataFrame(data=d)
print(df)

for i in range(len(banka)):
    plt.scatter(alis[i], satis[i], label=banka[i])
plt.xlabel("Alış")
plt.ylabel("Satış")
plt.legend(loc='lower right')
plt.show()
