import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = "https://flip.ro/magazin/?category=smartwatch"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.text, "html.parser")

ceas = soup.find_all('div', {'data-cy': 'phone-item'})

# nume
# pret
# link
lista_ceasuri = []

for i in ceas:

    nume = i.find("span",class_ = "block").text
    feature = i.find_all("span",class_ = "block")[1].text
    pret = i.find("span", {"data-cy" : "phone-price"}).text
    link = i.find("div", class_ = "flex items-center justify-center").img["srcset"]

    dictionar_ceas ={
        "Name": nume,
        "Features": feature,
        "Pret": pret,
        "Link": link
    }

    lista_ceasuri.append(dictionar_ceas)

with open("Ceasuri_Flip.txt", "w+") as file:
    json.dump(lista_ceasuri,file, indent=2)


df = pd.DataFrame(lista_ceasuri)
df.to_excel("Ceasuri_Flip.xlsx")
df.to_csv("Ceasuri_Flip.csv") 