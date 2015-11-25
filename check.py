import urllib2
import random
import string

letters = "abcdefghijklmnopqrstuvwxyz"


for j in "abcdefghijklm":
	for k in letters:
		for l in letters:
			url = "http://www."+i+j+k+l+".com"
			print url
			try:
			    urllib2.urlopen(url)
			    with open("output.txt", "a") as myfile:
			   		myfile.write(url + "\n")
			   		b+=1
			   		print b
			except:
				pass





