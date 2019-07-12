import bs4 as bs
import urllib.request
import traceback
source = urllib.request.urlopen('https://www.w3schools.com').read()
soup = bs.BeautifulSoup(source,'lxml')

try:
	for link in soup.find_all('a', href=True):
		if('.asp' in link['href']):
			source_next = urllib.request.urlopen('https://www.w3schools.com' + link['href']).read()
			soup_next = bs.BeautifulSoup(source_next,'lxml')
			for paragraph in soup.find_all('p'):
				print(str(paragraph.text))

			for link_next in soup_next.find_all('a', href=True):
				print(link_next.get('href'))
				if('.asp' in link_next['href']):
					source_new = urllib.request.urlopen('https://www.w3schools.com' + link_next['href']).read()
					soup_new = bs.BeautifulSoup(source_new,'lxml')
					for paragraph_new in soup_new.find_all('p'):
						print(str(paragraph_new.text))
						    with open('/home/soumi/Desktop/BeautifulSoup/BS.txt', 'a') as file:
						    	file.write(paragraph_new.text)

		
except:
	print (traceback.format_exc())
