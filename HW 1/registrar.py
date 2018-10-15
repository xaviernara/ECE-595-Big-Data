# Identifiers:
# \ used to escape a character
# \d any number
# \D anything but a number
# \s space
# \S anything but a space
# \w any character
# \W anything but a character
# . any character except a new line
# \. actually a period
# \b whitespace around words

# Modifiers:
# {1,3} we're expecting 1-3
# + Match 1 or more
# ? Match 0 or 1
# * Match 0 or more
# $ match the end of a string
# ^ match the beginning of a string
# | matches either or e.g. \d{1-3}|\w{5-6}
# [] Match range or "variance" e.g. [A-Za-z] or [1-5a-qA-Z]
# {x} expecting "x" amount

# White Space Characters:
# \n new line
# \s space
# \t tab
# \e escape (rare)
# \f form feed (rare)
# \r return

# DON'T FORGET!:
# . + * ? [ ] $ ^ ( ) { } \ |﻿


import re

#reading from a file
file_reader= open ("records.txt","r")
text= file_reader.read()
#print(text)
file_reader.close

#[A-Z][a-z]* finds all strings that begins with capital letters 
#and have any number lowercase letters afterwards
#Ex:I saw Jimmy found:Jimmy
studentNames = []
ece595 = []

#names = re.findall(r'[A-Z][a-z]*', text)
names = re.match(r'[A-Z][a-z]*', text)
class1 = re.findall(r',\d\d,',text)

with open("records.txt") as find:
   for text in find:
      #if names:
      if names :
         #studentNames.append(names)
         studentNames.append(names.group(0))
         #print("names:", studentNames)
      #(key,value) = line.re.findall(r'[A-Z][a-z]*')
      
      
      

print("names test:", studentNames)
    
     
      
      #studentNames[key] = value
     #print(studentNames)
      
      
#studentNamesre.findall(r'[A-Z][a-z]*',text)}



#ece595[]=
#ece547[]=
#ece354[]=


