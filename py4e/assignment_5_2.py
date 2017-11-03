largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        ival = int(num)
    except:
        print('Invalid input')
        continue

    if (largest is None) or (largest < ival):
        largest = ival

    if (smallest is None) or (smallest > ival):
        smallest = ival

print('Maximum is', largest)
print('Minimum is', smallest)
