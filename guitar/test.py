from Inventory  import *
from Guitar     import *
from Builder    import *
from Type       import *
from Wood       import *
from GuitarSpec import *
from Instrument import *

# abstract test
# aaa = Instrument("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6));

inventory = Inventory()
inventory.add_guitar("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6))
inventory.add_guitar("V9512", 1549.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6))

what_erin_likes = GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)

matching_guitars = inventory.search(what_erin_likes)

if matching_guitars:
    print("Erin, you might like this")

    for guitar in matching_guitars:
        spec = guitar.get_spec()

        output = '';
        output = "  We have a {builder} {model} {num_strings}-string {type} guitar:\n    {backwood} back and sides,\n    {topwood} top.\n  You can have it for only ${price}!\n  ---"
        output_tab =    {
                            'builder'       : spec.get_builder().value,
                            'model'         : spec.get_model(),
                            'type'          : spec.get_type().value,
                            'backwood'      : spec.get_back_wood().value,
                            'topwood'       : spec.get_top_wood().value,
                            'price'         : guitar.get_price(),
                            'num_strings'   : spec.get_num_strings()
                        }

        print(output.format(**output_tab))
else:
    print("Sorry, Erin, we have nothing for you.")