import os
import wiki

def wikki():
	c=0
	for file in os.listdir("DAT/"):
		if file.endswith(".txt"):
			c+=1
			print(c)
			file=file.lower()
			wiki.wiki("DAT/"+file)