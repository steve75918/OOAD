class Remote:
    _door = None

    def __init__(cls, door):
        cls._door = door

    def press_button(cls):
        print("Pressing the remote control button...")

        if cls._door.is_open() is True:
            cls._door.close()

            return  True
        else:
            cls._door.open()

            return True