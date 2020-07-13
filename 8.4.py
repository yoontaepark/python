fname = input("Enter file name: ") #input file name: romeo.txt
fh = open(fname)                   #open file 
lst = list()                       #initializing list variable 'lst'
for line in fh:                    #for all the lines in fh
    line = line.rstrip()           #erazing spaces from start & end & \n
    line = line.split()            #spliting by spaces in the midde 
    for i in line:                 # for all the words in line
        if i not in lst:           # add to lst (if not added)
            lst.append(i)

lst.sort()                         #sort in alphabetical order
print(lst)                         #print sorted order 
