# from Inventory import *
import Guitar

a = Guitar.Guitar('100', 2, '3', '4', '5', '6', '7')
# a = Inventory()
# a.add_guitar('1', 2, '3', '4', '5', '6', '7')
print(a.get_serial_number())
print(a.serial_number)
print(Guitar.Guitar.serial_number)