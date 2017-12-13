import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_40603.txt"

try:
    fh = open(fname)
except:
    print('Can not find file: ', fname)
    quit()

# using fh.read() to read whole file instead of a line. Notice the file size before do it
# using List comprehension to transform string into integer, then summary all
print(sum([int(i) for i in re.findall('[0-9]+', fh.read())]))
