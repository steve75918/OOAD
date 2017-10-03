from Inventory import *
from InstrumentType import *
from Builder import *
from Type import *
from Wood import *
from Style import *

# abstract test
# aaa = Instrument("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6));

inventory = Inventory()
# add guitar
instrument_spec = {'instrumentType': InstrumentType.GUITAR, 'builder': Builder.FENDER, 'model': "Stratocastor",
                   'type': Type.ELECTRIC, 'backWood': Wood.ALDER, 'topWood': Wood.ALDER, 'numStrings': 6}
inventory.add_instrument("V95693", 1499.95, instrument_spec)

instrument_spec = {'instrumentType': InstrumentType.GUITAR, 'builder': Builder.OLSON, 'model': "Stratocastor",
                   'type': Type.ELECTRIC, 'backWood': Wood.ALDER, 'topWood': Wood.ALDER, 'numStrings': 6}
inventory.add_instrument("V9512", 1549.95, instrument_spec)

# add mandolin
instrument_spec = {'instrumentType': InstrumentType.MANDOLIN, 'builder': Builder.MARTIN, 'model': "Stratocastor",
                   'type': Type.ELECTRIC, 'backWood': Wood.ALDER, 'topWood': Wood.ALDER, 'style': Style.F}
inventory.add_instrument("M1022", 2000.15, instrument_spec)

instrument_spec = {'instrumentType': InstrumentType.MANDOLIN, 'builder': Builder.FENDER, 'model': "Stratocastor",
                   'type': Type.ELECTRIC, 'backWood': Wood.SITKA, 'topWood': Wood.ALDER, 'style': Style.A}
inventory.add_instrument("M1028", 12231.99, instrument_spec)

what_guitar_erin_likes = {'instrumentType': InstrumentType.GUITAR, 'builder': Builder.FENDER,
                          'model': "Stratocastor", 'type': Type.ELECTRIC, 'backWood': Wood.ALDER, 'topWood': Wood.ALDER, 'numStrings': 6}
# what_madolin_erin_likes = MandolinSpec(Builder.MARTIN, "Stratocastor", Type.ELECTRIC, Style.A, Wood.ALDER, Wood.ALDER)

matching_guitars = inventory.search(what_guitar_erin_likes)

if matching_guitars:
    print("Erin, you might like this")

    for guitar in matching_guitars:
        spec = guitar.get_spec().get_properties()

        output = ''
        output = "  We have a {instrument_type} with following properties: \n  You can have it for only ${price}!\n  ---"
        output_tab = {
            'instrument_type': spec.get_property('instrumentType').value,
            'price': guitar.get_price(),
        }

        print(output.format(**output_tab))
else:
    print("Sorry, Erin, we have nothing for you.")

# matching_madolins = inventory.search(what_madolin_erin_likes)

# if matching_madolins:
#     print("Erin, you might like this")

#     for madolin in matching_madolins:
#         spec = madolin.get_spec()

#         output = '';
#         output = "  We have a {builder} {model} {type}-type {style}-style madolin:\n    {backwood} back and sides,\n    {topwood} top.\n  You can have it for only ${price}!\n  ---"
#         output_tab =    {
#                             'builder'       : spec.get_builder().value,
#                             'model'         : spec.get_model(),
#                             'type'          : spec.get_type().value,
#                             'backwood'      : spec.get_back_wood().value,
#                             'topwood'       : spec.get_top_wood().value,
#                             'price'         : madolin.get_price(),
#                             'style'         : spec.get_style().value
#                         }

#         print(output.format(**output_tab))
# else:
#     print("Sorry, Erin, we have nothing for you.")
