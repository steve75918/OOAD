from Inventory  import *
from Guitar     import *
from Builder    import *
from Type       import *
from Wood       import *

inventory = Inventory()
inventory.add_guitar("V95693", 1499.95, Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
inventory.add_guitar("V9512", 1549.95, Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER)

what_erin_likes = Guitar("", 0, Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER)

matching_guitars = inventory.search(what_erin_likes)

if matching_guitars:
    print("Erin, you might like this")

    for guitar in matching_guitars:
        output = '';
        output = "  We have a {builder} {model} {type} guitar:\n    {backwood} back and sides,\n    {topwood} top.\n  You can have it for only ${price}!\n  ---"

        print(output.format(builder = guitar.get_builder().value,
                      model = guitar.get_model(),
                      type = guitar.get_type().value,
                      backwood = guitar.get_back_wood().value,
                      topwood = guitar.get_top_wood().value,
                      price = guitar.get_price()
                        ))
else:
    print("Sorry, Erin, we have nothing for you.")