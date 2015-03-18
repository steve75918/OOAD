class Bark:
    _sound = ''

    def __init__(cls, sound):
        cls._sound = sound

    def get_sound(cls):
        return cls._sound

    def equals(cls, bark):
        if cls._sound == bark.get_sound():
            return True
        else:
            return False