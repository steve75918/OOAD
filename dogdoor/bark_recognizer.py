class BarkRecognizer:
    _door = None

    def __init__(cls, door):
        cls._door = door

    def recognize(cls, bark):
        print("    BarkReconginzer: Heard a '{bark}' ".format(bark=bark))
        cls._door.open()

        return True