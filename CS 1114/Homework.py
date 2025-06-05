
import copy
wordset=[]
wordstorage=[]
shortlist=[]
biglist=[]
bigwordlist=[]
listwords=["eat","tea","tan","ate","nat","bat"]
listwordscopy=copy.deepcopy(listwords)
for i in range(0,len(listwordscopy)):
    elementscopy=sorted(listwordscopy[i])
    listwordscopy[i]="".join(elementscopy)
for i in range(0,len(listwordscopy)):
    if listwordscopy[i] not in wordset:
        wordset.append(listwordscopy[i])
for elements1 in wordset:
    for i in range (0,len(listwordscopy)):
        if listwordscopy[i] == elements1:
            shortlist.append(listwords[i])
    biglist.append(shortlist)
    shortlist=[]
print(biglist)





        


    


# for words in listwords:

# .sort()