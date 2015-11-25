import urllib2
import random
import string


def randstring():
	url = "http://www."
	i = 0
	while i < 5:
		url = url + random.choice(string.ascii_lowercase)
		i += 1
	url = url + ".com"
	return url

b = 0
while b < 30:
	url = randstring();
	try:
	    urllib2.urlopen(url)
	    with open("Output.txt", "a") as myfile:
	   		myfile.write(url + "\n")
	   		b+=1
	   		print b
	except:
		pass





