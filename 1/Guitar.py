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

    def get_price():
        return price;

    def set_price():
        return true;

    def get_builder():
        return builder;

    def get_model():
        return model;

    def get_type():
        return type;

    def get_back_wood():
        return back_wood;

    def get_top_wood():
        return top_wood;