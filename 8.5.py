fname = input("Enter file name: ")           #input file name: mbox-short.txt
fh = open(fname)                             #open file
count = 0                                    #initialize variable count to 0

for line in fh:                              #check every line in fh
    line = line.rstrip()                     #remove front space, end space, and \n
    wds = line.split()                       #split line by () 
    
    if len(wds) < 1 or wds[0] != 'From':     #Guardian statement + filter condition
        continue

    print(wds[1])                            #print word that comes after 'From' 
    count += 1                               #add counts whenever there were printed words

print("There were", count, "lines in the file with From as the first word")  #print counts in a sentences 
