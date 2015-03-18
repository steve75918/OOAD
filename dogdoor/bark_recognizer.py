class BarkRecognizer:
    _door = None

    def __init__(cls, door):
        cls._door = door

    def recognize(cls, bark):
        print("    BarkReconginzer: Heard a '{bark}' ".format(bark=bark.get_sound()))

        allowed_barks = cls._door.get_allowed_barks()

        for allowed_bark in allowed_barks:
            if allowed_bark.equals(bark):
                cls._door.open()

                return True

        print("This dog is not allowed.");

        return True