hrs  = input("Enter Hours:")
rate = input("Enter rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Please enter a numeric input.')
    #we can't handle non numeric data, just quit before something blew up
    quit()

if h >= 40.0:
    plus_rate = 1.5

    h_base = 40.0 * r
    h_plus = (h - 40.0) * r * 1.5

    gross_pay = h_base + h_plus
else:
    gross_pay = h * r

print('Pay:', gross_pay)