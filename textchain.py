#!/usr/bin/python3

from itertools import chain
import re
import random

#settiing up the training text
speech = open("speech.txt", "r") #create a file with the training text
                                #and name it speech.txt
text = speech.readlines()
text = [x.strip() for x in text]
text = [x for x in text if x != '']
sample = []
for sentence in text:
    sample.append(sentence.split())
regex = re.compile('[^a-zA-Z]')
sample = list(chain(*sample))
for word in range(len(sample)):
    sample[word] = sample[word].lower()
    sample[word] = regex.sub('', sample[word])

mappings = {}

#mappings
for i in range(len(sample)-1): #the analysis is 1 word ahead of the key
    values = []
    key = sample[i]
    indices = [i for i, x in enumerate(sample) if x == key]
    for index in indices:
        if index < len(sample)-1: 
            values.append(sample[index+1])
    mappings[key] = values

#the actual text output
text = [random.choice(list(mappings.keys()))]
length = 100
j = 0
for i in range(length-1):
    current_key = text[j]
    if len(mappings[current_key]) > 0:
        text.append(random.choice(list(mappings[current_key])))
    else:
        text.append(random.choice(list(mappings)))
    j += 1

#Capitalize the first word
text[0] = text[0].capitalize()

text = ' '.join(text)

print(text)
        

  
    



