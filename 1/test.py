from Inventory  import *
from Guitar     import *
from Builder    import *
from Type       import *
from Wood       import *

inventory = Inventory()
inventory.add_guitar("V95693", 1499.95, "Fender", "Stratocastor", "electric", "Alder", "Alder")

what_erin_likes = Guitar("", 0, Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER)

guitar = inventory.search(what_erin_likes)

if guitar is not None:
    output = '';
    output = "Erin, you might like this {builder} {model} {type} guitar: \n{backwood} back and sides, \n{topwood} top.\nYou can have it for only ${price}!"
    output.format(builder = guitar.get_builder,
                  model = guitar.get_model(),
                  type = guitar.get_type(),
                  backwood = guitar.get_back_wood(),
                  topwood = guitar.get_top_wood(),
                  price = guitar.get_price(),
                    )

    print(output)
else:
    print("Sorry, Erin, we have nothing for you.")