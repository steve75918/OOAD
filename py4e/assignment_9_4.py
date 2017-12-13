fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('Can not find file: ', fname)
    quit()

#build a histogram of email and send times
counts = dict()
for line in fh:
    # only prase line have email
    if not line.startswith('From '):
        continue

    words = line.split()

    email = words[1]
    counts[email] = counts.get(email, 0) + 1

big_count = 0
big_count_sender = ''
for mail_acc in counts:
    count = counts[mail_acc]
    if count is None or count > big_count:
        big_count_sender = mail_acc
        big_count = count

print(big_count_sender, big_count)
