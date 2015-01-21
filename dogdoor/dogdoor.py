import threading

class DogDoor:
    _open = False;

    def __init__(cls):
        cls._open = False

    def open(cls):
        print("The dog door opens.")
        cls._open = True

        # auto close dogdoor after 5 seconds
        task = threading.Timer(5, cls.close)
        task.start()

        return True

    def close(cls):
        print("The dog door closes.")
        cls._open = False
        return True

    def is_open(cls):
        return cls._open