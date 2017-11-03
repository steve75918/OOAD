hrs  = input("Enter Hours:")
h = float(hrs)

rate = input("Enter rate:")
r = float(rate)

if h >= 40.0:
    plus_rate = 1.5

    h_base = 40.0 * r
    h_plus = (h - 40.0) * r * 1.5

    gross_pay = h_base + h_plus
else:
    gross_pay = h * r

print('Pay:', gross_pay)