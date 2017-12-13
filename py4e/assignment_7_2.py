# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Can not find file: ', fname)
    quit()

line_cnt = 0
value_cnt = 0
value_total = 0
for line in fh:
    # count line
    line_cnt = line_cnt + 1

    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # find the string position for float number
    pos = line.find('0.')
    try:
        fval = float(line[pos:])
    except:
        print('Something is not string at line:', line_cnt)

    # count value
    value_cnt = value_cnt + 1
    value_total = value_total + fval

avg = value_total / value_cnt
print("Average spam confidence:", avg)
