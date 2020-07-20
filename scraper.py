import requests
from bs4 import BeautifulSoup


URL = input()
r1 = requests.get(URL)

soup1 = BeautifulSoup(r1.content, 'html5lib')

li1 = soup1.find_all('a', href=True)
print(soup1.title.string)

for l1 in li1:
	try:
		r2 = requests.get(l1['href'])
		soup2 = BeautifulSoup(r2.content, 'html5lib')
		print('\t{}'.format(soup2.title.string))
		li2 = soup2.find_all('a', href=True)
		
		for l2 in li2:
			try:
				r3 = requests.get(l2['href'])
				soup3 = BeautifulSoup(r3.content, 'html5lib')
				print('\t\t{}'.format(soup3.title.string))
			except:
				pass
	except:
		pass
