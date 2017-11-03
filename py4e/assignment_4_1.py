def computepay(h:float, r:float):
    p_base = h * r

    if h >= 40.0:
        plus_rate = 0.5
        
        p_plus = (h - 40.0) * r * plus_rate
    else:
        p_plus = 0.0

    gross_pay = p_base + p_plus

    return gross_pay

hrs  = input("Enter Hours:")
rate = input("Enter rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Please enter a numeric input.')
    #we can't handle non numeric data, just quit before something blew up
    quit()

p = computepay(h, r)
print("Pay", p)
