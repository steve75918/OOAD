fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('Can not find file: ', fname)
    quit()

count = 0
for line in fh:
    # only prase line have email
    if not line.startswith('From '):
        continue

    words = line.split()

    email = words[1]
    print(email)

    count = count + 1

print("There were", count, "lines in the file with From as the first word")
