from bs4 import BeautifulSoup
import requests
import pandas as pd


# Ce projet consiste en un script de web scraping qui extrait des informations sur des pays à partir d'un site web donné.
# Les données collectées sont ensuite organisées sous forme de tableau (DataFrame) à l'aide de la bibliothèque pandas.
# Le but est de sauvegarder ces informations dans un fichier Excel, afin de faciliter leur manipulation et analyse ultérieure.
# Ce projet utilise les bibliothèques suivantes : requests (pour récupérer les données), BeautifulSoup (pour parser le HTML),
# pandas (pour organiser et exporter les données)


url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)
soup = BeautifulSoup(response.text , 'html.parser') #on peut même utiliser 'lxml' à la place de 'html.parser' parceque il est plut performent et rapide
rows = soup.find('table',{'id':'example2'}).find('tbody').find_all('tr')

countries_list = []
for row in rows :
    dic = {}
    dic['countries'] = row.find_all('td')[1].text
    dic['population 2024'] = row.find_all('td')[2].text

    countries_list.append(dic)



#sauvegarder dans fichier excel/csv

df = pd.DataFrame(countries_list)

# Exporter vers Excel
df.to_excel('countries_list.xlsx', index=False)

# Exporter vers CSV
df.to_csv('countries_list.csv', index=False)


