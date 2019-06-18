from Inventory import *
from InstrumentSpec import *
from InstrumentType import *
from Builder import *
from Type import *
from Wood import *
from Style import *

# add group of instruments into invenroty for test
def initializeInventory(inventory):

    specList = []

    # add guitar 11277
    properties = {}

    properties['instrument_type'] = InstrumentType.GUITAR
    properties['builder']         = Builder.COLLINGS
    properties['model']           = "CJ"
    properties['type']            = Type.ACOUSTIC
    properties['num_strings']     = 6
    properties['back_wood']       = Wood.INDIAN_ROSEWOOD
    properties['top_wood']        = Wood.SITKA

    spec = {}
    spec['SerialNo'] = "11277"
    spec['Value']    = 3999.95
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    # add guitar 122784
    properties = {}

    properties['instrument_type'] = InstrumentType.GUITAR
    properties['builder']         = Builder.MARTIN
    properties['model']           = "D-18"
    properties['type']            = Type.ACOUSTIC
    properties['num_strings']     = 6
    properties['back_wood']       = Wood.MAHOGANY
    properties['top_wood']        = Wood.ADIRONDACK

    spec = {}
    spec['SerialNo'] = "122784"
    spec['Value']    = 5495.95
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    # add guitar V95693
    properties = {}

    properties['instrument_type'] = InstrumentType.GUITAR
    properties['builder']         = Builder.FENDER
    properties['model']           = "Stratocaster"
    properties['type']            = Type.ELECTRIC
    properties['num_strings']     = 6
    properties['back_wood']       = Wood.ALDER
    properties['top_wood']        = Wood.ALDER

    spec = {}
    spec['SerialNo'] = "V95693"
    spec['Value']    = 1499.95
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    # add guitar V9512
    properties = {}

    properties['instrument_type'] = InstrumentType.GUITAR
    properties['builder']         = Builder.FENDER
    properties['model']           = "Stratocaster"
    properties['type']            = Type.ELECTRIC
    properties['num_strings']     = 6
    properties['back_wood']       = Wood.ALDER
    properties['top_wood']        = Wood.ALDER

    spec = {}
    spec['SerialNo'] = "V9512"
    spec['Value']    = 1549.95
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    # add guitar 82765501
    properties = {}

    properties['instrument_type'] = InstrumentType.GUITAR
    properties['builder']         = Builder.GIBSON
    properties['model']           = "SG '61 Reissue"
    properties['type']            = Type.ELECTRIC
    properties['num_strings']     = 6
    properties['back_wood']       = Wood.MAHOGANY
    properties['top_wood']        = Wood.MAHOGANY

    spec = {}
    spec['SerialNo'] = "82765501"
    spec['Value']    = 1890.95
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    # add guitar 70108276
    properties = {}

    properties['instrument_type'] = InstrumentType.GUITAR
    properties['builder']         = Builder.GIBSON
    properties['model']           = "Les Paul"
    properties['type']            = Type.ELECTRIC
    properties['num_strings']     = 6
    properties['back_wood']       = Wood.MAPLE
    properties['top_wood']        = Wood.MAPLE

    spec = {}
    spec['SerialNo'] = "70108276"
    spec['Value']    = 2295.95
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    # add Mandolin 9019920
    properties = {}

    properties['instrument_type'] = InstrumentType.MANDOLIN
    properties['builder']         = Builder.GIBSON
    properties['model']           = "F5-G"
    properties['type']            = Type.ACOUSTIC
    properties['back_wood']       = Wood.MAPLE
    properties['top_wood']        = Wood.MAPLE

    spec = {}
    spec['SerialNo'] = "9019920"
    spec['Value']    = 5495.99
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    # add Banjo 8900231
    properties = {}

    properties['instrument_type'] = InstrumentType.BANJO
    properties['builder']         = Builder.GIBSON
    properties['model']           = "RB-3"
    properties['num_strings']     = 5
    properties['type']            = Type.ACOUSTIC
    properties['back_wood']       = Wood.MAPLE

    spec = {}
    spec['SerialNo'] = "8900231"
    spec['Value']    = 2945.95
    spec['instrumentSpec'] = InstrumentSpec(properties)

    specList.append(spec)

    del spec, properties

    for s in specList:
        inventory.add_instrument(s['SerialNo'], s['Value'], s['instrumentSpec'])

    return

# main
inventory = Inventory()
initializeInventory(inventory)

# customer wanted
properties = {}
properties['builder']         = Builder.GIBSON
properties['back_wood']       = Wood.MAPLE

clientSpec = InstrumentSpec(properties)

matchingInstruments = inventory.search(clientSpec)

if matchingInstruments:
    print("You might like this")

    for instrument in matchingInstruments:
        spec = instrument.get_spec()

        output = "    We have a serial #{} with following properties: \n".format(instrument.get_serial_number())
        print(output)

        for p_name, p_value in spec.get_properties().items():
            if isinstance(p_value, Enum):
                print("    {p_name}: {p_value}".format(p_name = p_name, p_value = p_value.value))
            else:
                print("    {p_name}: {p_value}".format(p_name = p_name, p_value = p_value))

        print("\n    You can have it for only ${}!\n    ---".format(instrument.get_price()))
else:
    print("Sorry, we have nothing for you.")
