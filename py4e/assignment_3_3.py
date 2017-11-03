score = input("Enter Score: ")

#sense check of input
try:
    s = float(score)
except:
    print('Please enter numeric score between 0.0 to 1.0.')
    quit()

if s < 0:
    print('Error! Score smaller than 0.0')
elif s < 0.6:
    print('F')
elif s < 0.7:
    print('D')
elif s < 0.8:
    print('C')
elif s < 0.9:
    print('B')
elif s <= 1.0:
    print('A')
else:
    print('Error! Score greater than 1.0')