import re                              #to use re.findall function

hand = open("regex_sum_731536.txt")    #open file
x=list()                               #make a null list
for line in hand:                      #for all lines in txt file
     y = re.findall('[0-9]+',line)     #findall numbers
     x = x+y                           #add to list, at this moment, x is just list of numbers

sum=0                                  #make sum variable and initialize
for z in x:                            #for all numbers in list
    sum = sum + int(z)                 #transfer all numbers into interger and sum

print(sum)                             #print out sum 
