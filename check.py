import urllib2
from bs4 import BeautifulSoup
import random
import string

letters = "abcdefghijklmnopqrstuvwxyz"


for j in "abcdefghijklm":
	for k in letters:
		for l in letters:
			url = "http://www."+j+k+l+".com"
			try:
				rawdata = urllib2.urlopen(url)
				soup = BeautifulSoup(rawdata, 'html.parser')
				title = soup.title.string
				print title

				desc = soup.find(attrs={"name":"description"}) 
				if desc:
					desc = desc.encode('utf-8')
				else:
					desc = "geen omschrijving gevonden"
				

				with open("output.txt", "a") as myfile:
					myfile.write("url: " + url + "\n"  + "Omshcrijving: " + desc + "\n" + "Title: " + title + "\n\n")
					b+=1
					print b
			except:
				pass


# for j in "abcdefghijklm":
# 	for k in letters:
# 		for l in letters:
# 			url = "http://www."+j+k+l+".com"
# 			print url
# 			try:
# 			    urllib2.urlopen(url)
# 			    with open("output.txt", "a") as myfile:
# 			   		myfile.write(url + "\n")
# 			   		b+=1
# 			   		print b
# 			except:
# 				pass


