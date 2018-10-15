#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	# Important to begin by printing every line 
	# To see where to split the string
	#print(line)
	words = line.split('\t') # Needs to be split at every '\t'
	#print(words)	
	city = words[2]	
	sale = words[4]
	print('%s\t%s'%(city, sale))