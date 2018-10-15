#!/usr/bin/python

import sys

(last_host, last_http) = (None, None)

for line in sys.stdin:
	(host, http) = line.split('\t')
	if last_host and host != last_host or http != last_http:
		print('%s\t%s'%(last_host, last_http))
		(last_host, last_http) = (host, http)
#	else:
#		(last_key, count) = (key, count+1)

if last_host:
	print('%s\t%s'%(last_host, last_http))