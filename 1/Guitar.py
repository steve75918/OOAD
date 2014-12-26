class Guitar:
    serial_number = '10000'
    price         = 0.0
    builder       = ''
    model         = ''
    type          = ''
    back_wood     = ''
    top_wood      = ''

    def __init__(self, serial_number, price, builder, model, type, back_wood, top_wood):
        self.serial_number  = serial_number
        self.price          = price
        self.builder        = builder
        self.model          = model
        self.type           = type
        self.back_wood      = back_wood
        self.top_wood       = top_wood
        print("1")

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, value):
        self.price = value

    def get_builder(self):
        return self.builder

    def get_model(self):
        return self.model

    def get_type(self):
        return self.type

    def get_back_wood(self):
        return self.back_wood

    def get_top_wood(self):
        return self.top_wood