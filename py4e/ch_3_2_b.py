rawstr = input('Please input a number:')
#this program can not deal with type a negative number, e.q: -42
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
