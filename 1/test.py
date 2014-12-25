class Guitar:
    serial_number;
    price;
    builder;
    model;
    type;
    back_wood;
    top_wood;

    def __init__(self, serial_number, price, builder, model, type, back_wood, top_wood):
        self.serial_number  = serial_number;
        self.price          = price;
        self.builder        = builder;
        self.model          = model;
        self.type           = type;
        self.back_wood      = back_wood;
        self.top_wood       = top_wood;

    def get_serial_number():
        return serial_number;


a = Guitar('1', 2, '3', '4', '5', '6', '7');
a.get_serial_number();