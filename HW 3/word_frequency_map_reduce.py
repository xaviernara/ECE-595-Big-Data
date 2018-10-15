import sys


for line in sys.stdin:
   
   #strips the whitespace off of the text file strings
    line = line.strip()
    
    #splits the text file strings at the 1st space 
    #when the string is split its split into array 
    words = line.split(' ')
    
    for word in words:
    
      #splits the text file strings at the 1st ' " '  
   	word = word.split('"')
      
      #the 1st array string element is placed into the string word
   	word = word[-1].lower()
      
      #isalpha() true if all the chars in the string are alphabets in it 
      #false if the string contains 1 or more no-alphabets
   	if word.isalpha():
           	print('%s\t%s'%(word, 1))