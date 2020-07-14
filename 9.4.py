fname = input("Enter file:")                    #opening file
if len(fname) < 1 : name = "mbox-short.txt"     #opening file w/o typeing file(just enter works)
hand = open(fname)                              #name hand as txt file
di = dict()                                     #make empty dictionary and name as di

for line in hand:                               #check all lines in txt file
    #line = line.rstrip()                       #rstrip is actually not needed if split function is used(split function includes rstrip)
    wds = line.split()                          #use split function and name wds   
    if len(wds)<1 or wds[0] != 'From': continue #guardian fuction to except all w/o 'From' lines
    di[wds[1]] = di.get(wds[1],0) + 1           #count the value of wds[1] since i want to know value of wds[1] (it is an idiom)
     
largest = None                                  #name largest value and initialize
theword = None                                  #name largest key and initialize
for k,v in di.items():                          #for all (key,value)
    if v>largest:                               #if value is larger than previous one
        largest = v                             #update value
        theword = k                             #update key
        
print(theword, largest)                         #print (key, value) 
