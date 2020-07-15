name = input("Enter file:")                     #open file
if len(name) < 1 : name = "mbox-short.txt"      #open file
handle = open(name)                             #file name 
di = dict()                                     #make null dict

for line in handle:                             #for all lines in txt
    wds = line.split()                          #split all lines(make them words w/o spaces)
    if len(wds)<1 or wds[0] != 'From': continue #erasing all lines except 'From'
    wds = wds[5]                                #just take 6th word (ex. 09:14:16) 
    wds = wds[:2]                               #in 6th word, just take 2 front words(0,1 => 09)
    di[wds] = di.get(wds,0) + 1                 #add couunts, and this will make di = (key, value)

for k,v in sorted(di.items()):                  #loop all (k,v) and sort in ascending order
    print(k,v)                                  #print all (k,v) pairs 
    
