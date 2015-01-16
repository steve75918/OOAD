class Remote:
    _door = None

    def __init__(cls, door):
        cls._door = door

    def press_button(cls):
        print("Pressing the remote control button...")

        if cls._door.is_open() is True:
            return cls._door.close()
        else:
            return cls._door.open()