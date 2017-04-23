from Inventory    import *
from Builder      import *
from Type         import *
from Wood         import *
from Style        import *
from GuitarSpec   import *
from MandolinSpec import *

# abstract test
# aaa = Instrument("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6));

inventory = Inventory()
# add guitar
inventory.add_instrument("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6))
inventory.add_instrument("V9512", 1549.95, GuitarSpec(Builder.OLSON, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6))

# add mandolin
inventory.add_instrument("M1022", 1590.95, MandolinSpec(Builder.MARTIN, "Stratocastor", Type.ELECTRIC, Style.A, Wood.ALDER, Wood.ALDER))
inventory.add_instrument("M1028", 1590.95, MandolinSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Style.F, Wood.ALDER, Wood.ALDER))

#what_erin_likes = GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
what_erin_likes = MandolinSpec(Builder.MARTIN, "Stratocastor", Type.ELECTRIC, Style.A, Wood.ALDER, Wood.ALDER)

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