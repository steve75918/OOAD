from Inventory import *
from InstrumentSpec import *
from InstrumentType import *
from Builder import *
from Type import *
from Wood import *
from Style import *

inventory = Inventory()

# add guitar
spec = {}
spec['instrument_type'] = InstrumentType.GUITAR
spec['builder']         = Builder.FENDER
spec['type']            = Type.ELECTRIC
spec['back_wood']       = Wood.ALDER
spec['top_wood']        = Wood.ALDER
spec['num_strings']     = 6
spec['model']           = "Stratocastor"

instrument_spec = InstrumentSpec(spec)

inventory.add_instrument("V95693", 1499.95, instrument_spec)
del spec, instrument_spec

spec = {}
spec['instrument_type'] = InstrumentType.GUITAR
spec['builder']         = Builder.OLSON
spec['model']           = "Stratocastor"
spec['type']            = Type.ACOUSTIC
spec['top_wood']        = Wood.MAPLE
spec['back_wood']       = Wood.MAHOGANY
spec['num_strings']     = 6

instrument_spec = InstrumentSpec(spec)

inventory.add_instrument("DV200", 1099.50, instrument_spec)
del spec, instrument_spec

# # add mandolin
spec = {}
spec['instrument_type'] = InstrumentType.MANDOLIN
spec['builder']         = Builder.GIBSON
spec['model']           = "Minecraft"
spec['type']            = Type.ACOUSTIC
spec['top_wood']        = Wood.MAPLE
spec['back_wood']       = Wood.MAHOGANY
spec['style']           = Style.F

instrument_spec = InstrumentSpec(spec)

inventory.add_instrument("M170", 500.00, instrument_spec)
del spec, instrument_spec

spec = {}
spec['instrument_type'] = InstrumentType.MANDOLIN
spec['builder']         = Builder.GIBSON
spec['model']           = "Minecraft"
spec['type']            = Type.ACOUSTIC
spec['top_wood']        = Wood.MAPLE
spec['back_wood']       = Wood.BRAZILIAN_ROSEWOOD
spec['style']           = Style.A

instrument_spec = InstrumentSpec(spec)

inventory.add_instrument("M1028", 1350.75, instrument_spec)
del spec, instrument_spec

# erin_likes_guitar
# what_erin_likes = {}
# what_erin_likes['instrument_type'] = InstrumentType.GUITAR
# what_erin_likes['builder']         = Builder.FENDER
# what_erin_likes['model']           = "Stratocastor"
# what_erin_likes['type']            = Type.ELECTRIC
# what_erin_likes['back_wood']       = Wood.ALDER
# what_erin_likes['top_wood']        = Wood.ALDER
# what_erin_likes['num_strings']     = 6

# erin_likes_mandolin
what_erin_likes = {}
what_erin_likes['instrument_type'] = InstrumentType.MANDOLIN
what_erin_likes['builder']         = Builder.GIBSON
what_erin_likes['model']           = "Minecraft"
what_erin_likes['type']            = Type.ACOUSTIC
what_erin_likes['top_wood']        = Wood.MAPLE
what_erin_likes['back_wood']       = Wood.BRAZILIAN_ROSEWOOD
what_erin_likes['style']           = Style.A

matching_instruments = inventory.search(what_erin_likes)

if matching_instruments:
    print("Erin, you might like this")

    for instrument in matching_instruments:
        spec = instrument.get_spec()

        output = "    We have a {} with following properties: \n".format(spec.get_property('instrument_type').value)
        print(output)

        for p_name, p_value in spec.get_properties().items():
            if isinstance(p_value, Enum):
                print("    {p_name}: {p_value}".format(p_name = p_name, p_value = p_value.value))
            else:
                print("    {p_name}: {p_value}".format(p_name = p_name, p_value = p_value))

        print("\n    You can have it for only ${}!\n    ---".format(instrument.get_price()))
else:
    print("Sorry, Erin, we have nothing for you.")
