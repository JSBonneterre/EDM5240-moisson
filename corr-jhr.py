# coding : utf-8

### BONJOUR, ICI Jean-Hugues ###
### Comme toujours, mes notes et corrections sont précédées de trois dièses ###

### Tout d'abord, il manque de commentaires dans ton code pour m'expliquer ce que tu cherches à faire
### Avec les noms de tes variables, on comprend que tu ne recueilles que les annonces de BMW dans LesPAC

import csv
import requests
from bs4 import BeautifulSoup

fichier2 = "moisson-bmw.csv"

for n in range(1,134):

	url = "https://www.lespac.com/montreal/bmw_b286df286dh0g17567i1j3k{}R1.jsa".format(n)
	#print(url)

	contenu = requests.get(url)
	page = BeautifulSoup(contenu.text,"html.parser")
	#print(page)

	urlChars = page.find_all("h2", class_="title")
	#print(urlChars)

	for urlBMW in urlChars:
		
		try:
			bmw = []
			
			url2 = urlBMW.a["href"]
			url2 = "https://www.lespac.com" + url2

			# print(url2)

### Il faudrait enregistrer l'URL dans ton fichier CSV afin de faire des «spot checks»
### et aussi pour vérifier des infos en apparence aberrantes
### Par exemple, une annonce indique un kilométrage de 8km seulement!!

			contenu2 = requests.get(url2)
			page2 = BeautifulSoup(contenu2.text,"html.parser")

			titre = page2.find("h1", id="productTitleH1").text
			print(titre)
			bmw.append(titre)

			prix = page2.find("div", class_="price").text
			print(prix)
			bmw.append(prix)
			
			# année =  page2.find("p", span="année").text
			# print(année)

			# tout = page2.find("div", class_="box").text
			# print(tout)
			# bmw.append(tout)
      # j'ai essayé bien des affaires avant de trouver une réponse sur Stack OverFlow! j'ai même pensé à faire sortir toute la boite de description, mais toutes les infos allaient dans une même cellule sur excel.

			annee = page2.find(text = "Année").find_next("a").text
			print(annee)
			bmw.append(annee)

			kilo = page2.find(text = "Kilométrage").find_next("span").text
			print(kilo)
			bmw.append(kilo)

			
			

			print(bmw)

			f2 = open(fichier2, "a")
			xyz = csv.writer(f2)
			xyz.writerow(bmw)

		except:
			print ("Y'a rien ici")
