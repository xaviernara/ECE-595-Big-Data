#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split(' ')
	
#	print(words)
	
	host = words[0]
	request = words[2] # Retrieves the http request	
	request = request.strip('"') # Splits at the " to get the type of request from: "GET or "POST
	
	words = line.split('"')
#	print(words)

	# print('%s\t%s'%(request, 1))
	# print(request, "2") -- if printed using this commnad 
	# code will print in this style: ('"GET', '2') 
	# Request = "GET in this example
	
	if request == "GET":
		http = words[1][4:]
		print('%s\t%s'%(host,http))