#!/usr/bin/python

import sys
(current_store, tot_sales) = (None, 0.0)
for line in sys.stdin:
	#print(line)
	(store, sale) = line.split('\t')
	#print(store, sale)
	if current_store and store != current_store:
		print('%s\t%s'%(current_store, tot_sales))
		(current_store, tot_sales) = (store, float(sale))
	else:
		(current_store, tot_sales) = (store, tot_sales + float(sale))

if current_store:
	print('%s\t%s'%(current_store, tot_sales))