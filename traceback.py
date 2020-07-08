#traceback: preventing errors or testing some lines but not to make error messages

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)
