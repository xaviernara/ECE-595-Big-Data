import re
import string

#declaring a empty dictionary 
#since we need key-value pairs, where key is the word, and the value represents the 
#frequency words appeared in the document.
frequency = {}

#The first thing we want to do is to store the text file in a string variable.
document_text = open('pg20417.txt','r')
text_string = document_text.read()

#Now, in order to make applying our regular expression easier, let's turn all the letters 
#in our document into lower case letters, using the lower() function, as follows:
text_string = document_text.read().lower()

#Let's write our regular expression that would return all the words with the number of characters in the range [3-15]. 
#Starting from 3 will help in avoiding words that we may not be interested in counting their frequency like if, of, in, etc., 
#and words having a length larger than 15 might not be correct words. The regular expression for such a pattern looks as follows:
#match_pattern = re.search(r'\b[a-z]{3,15}\b', text_string)
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)



for word in match_pattern:
    count = frequency.get(word,0)
    frequecny[word] = count + 1

#declaring a list for the words in the text file(ie keys) 
frequency_list = frequency.keys()

#in order to get the word and its frequency (number of times it appeared in the text file), we can do the following:
for words in frequency_list:
    print (words, frequency[words])
