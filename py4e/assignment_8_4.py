fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Can not find file: ', fname)
    quit()

lst = list()
for line in fh:
    words = line.split()

    # check the word in the list, append if is not
    for word in words:
        if word not in lst:
            lst.append(word)

# after grap all distinct word, sort it
lst.sort()

print(lst)
