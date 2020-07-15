fhand = open('romeo.txt')                       #open file
counts = dict()                                 #make dict type variable
for line in fhand:                              #for all lines in txt
    words = line.split()                        #split all lines, which means to split into words(rstrip is not needed)
    for word in words:                          #for all words
        counts[word] = counts.get(word, 0) + 1  #make histogram for each words

lst = list()                                    #make list type variable
for key, val in counts.items()                  #for tuple type counts(counts.item means tuple)
    newtup = (val, key)                         #name new variable in reversed match(key, value → value,key)
    lst.append(newtup)                          #list up all reversed items

lst = sorted(lst, reverse=True)                 #reverse sort(by value, biggest → smallest)

for val, key in lst[:10] :                      #for all (val, key) combination, loop only for 0~9(top 10)
    print(key, val)                             #print(val, key)

# or in one Line(shorter version: List comprehension)
#c = {'a':10, 'b':1, 'c':22} 
#print(sorted([ (v,k) for k,v in c.items() ]))
