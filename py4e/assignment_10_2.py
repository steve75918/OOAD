fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('Can not find file: ', fname)
    quit()

# build a histogram of hour
data_counts = dict()
for line in fh:
    # only prase line have time
    if not line.startswith('From '):
        continue

    words = line.split()
    time = words[5].split(':')

    hour = time[0]
    data_counts[hour] = data_counts.get(hour, 0) + 1

data_list = data_counts.items()

for k, v in sorted(data_counts.items()):
    print(k, v)
