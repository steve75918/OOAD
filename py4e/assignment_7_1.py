# Use words.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Please enter \'words.txt\' as file name.')
    quit()

for line in fh:
    print(line.rstrip().upper())