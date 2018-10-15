#!/usr/bin/python
import sys

#declaring a dict
#since we need key-value pairs, where key is the word, and the value represents the 
#frequency words appeared in the document.
(last_key, count) = (None, 0)

#the indivdual words from the text file
words = []

#the frequency of each word in the text file
values = []

for line in sys.stdin:

   
	(key, value) = line.split('\t')
	if last_key and key != last_key:
      #print('%s\t%s'%(last_key, count))
		words.append(last_key)
		values.append(count)
	        (last_key, count) = (key, int(value))
	else:
		(last_key, count) = (key, count+1)

if last_key:
   #print('%s\t%s' % (last_key, count))
	words.append(last_key)
	values.append(count)	

# Insertion Sort in decreasing order
for i in range(1,len(words)):
	key_word = words[i]
	key_value = values[i]
	j = i - 1
	
	while j >= 0 and values[j] < key_value:
		words[j + 1] = words[j] 
		values[j + 1] = values[j]
		j = j - 1
	
	words[j + 1] = key_word
	values[j + 1] = key_value

# Print first 10 in each list
for i in range(0,10):
	print('%s\t%s'%(words[i], values[i]))