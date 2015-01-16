class DogDoor:
    _open;

    def open(cls):
        print("The dog door opens.")
        cls._open = True

    def close(cls):
        print("The dog door closes.")
        cls._open = False

    def is_open(cls):
        return cls._open