class Printer():
    def __init__(self) -> None:
        pass

    @staticmethod
    def print_route(routes: list)->None:
        for connection in routes:
            print(
                'On line {line_name}, from {start} to {end}'
                .format(
                    line_name = connection.get_line_name(),
                    start     = connection.get_station1().get_name(),
                    end       = connection.get_station2().get_name()
                )
            )
        pass