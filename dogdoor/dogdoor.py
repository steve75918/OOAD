import threading

class DogDoor:
    _open = False
    _auto_close_time = 0
    _allowed_barks = []

    def __init__(cls, time=5):
        cls._open = False
        cls._auto_close_time = time

    def open(cls):
        print("The dog door opens.")
        cls._open = True

        # auto close dogdoor after 5 seconds
        task = threading.Timer(cls._auto_close_time, cls.close)
        task.start()

        return True

    def close(cls):
        print("The dog door closes.")
        cls._open = False
        return True

    def is_open(cls):
        return cls._open

    def add_allowed_bark(cls, bark):
        cls._allowed_barks.append(bark)

        return True

    def get_allowed_barks(cls):
        return cls._allowed_barks