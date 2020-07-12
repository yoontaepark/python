fname = input('Enter file name: ')
fh = open('words.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())


# use rstrip function to blow white spaces
# use .upper function to change the contents of the file in upper case 
