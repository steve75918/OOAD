from Inventory import *
# import Guitar

# a = Guitar.Guitar('100', 2, '3', '4', '5', '6', '7')
a = Inventory()
a.add_guitar('1', 2, '3', '4', '5', '6', '7')
a.add_guitar('2', 2, '3', '4', '5', '6', '7')

result = a.get_guitar('3')
print(result)
print(result.get_serial_number())