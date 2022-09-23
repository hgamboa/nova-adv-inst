#count the most used in lusiadas 

import collections

print('Reading text')

file = open('pg3333.txt', encoding="utf8")
text = file.read()
file.close()

print(text[0:40])
print(type(text))

l=text.lower().split()
print('\nlist\n',l[0:10])

mydict={}

for word in l:
    if word not in mydict:
        mydict[word] = 1
    else:
        mydict[word] +=1 

#print(mydict)

word_counter = collections.Counter(mydict)

#the most used word
print('word most used is: ', 
      word_counter.most_common(1)[0][0],
      '(', word_counter.most_common(1)[0][1], 
      'times )')

#the 10 most used words
print('\nThe 10 most used words')
for word, count in word_counter.most_common(10):
    print(word, ": ", count)










print(type(text))
print(text[0:40])

wordcount = {} #initialize dictionary
print(type(wordcount))

for word in text.lower().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] +=1
        
        
#print(wordcount)       
word_counter = collections.Counter(wordcount)

#the most used word
print('word most used is: ', 
      word_counter.most_common(1)[0][0],
      '(', word_counter.most_common(1)[0][1], 
      'times )')

#the 10 most used words
print('\nThe 10 most used words')
for word, count in word_counter.most_common(10):
    print(word, ": ", count)