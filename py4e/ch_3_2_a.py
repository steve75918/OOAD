x = int(input('Please input a number:'))

if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:
    #which can't execute
    print('Below 10')
else:
    print('Somthing else')