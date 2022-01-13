class Printer():
    def __init__(self) -> None:
        pass

    @staticmethod
    def print_route(routes: list)->None:
        previous = routes[0]

        for i in list(range(len(routes))):
            current = routes[i]

            if i == 0:
                # start
                print(
                    'Start out at {start}.\n\nGet on the {line_name} towards {end}.\n'
                    .format(
                        line_name = current.get_line_name(),
                        start     = current.get_station1().get_name(),
                        end       = current.get_station2().get_name()
                    )
                )
            elif i == len(routes) - 1:
                # end
                print(
                    '    Continue past {station_name}...\n'
                    .format(
                        station_name = current.get_station1().get_name(),
                    )
                ) 
                print(
                    'Get off at {end} and enjoy your self!'
                    .format(
                        end       = current.get_station2().get_name()
                    )
                )
            else:
                print(
                    '    Continue past {station_name}...\n'
                    .format(
                        station_name = current.get_station1().get_name(),
                    )
                ) 
                if previous.get_line_name() != current.get_line_name():
                    # need change line
                    print(
                        'When you get to {station_name}, get off the {line_name}'
                        .format(
                            station_name = previous.get_station2().get_name(),
                            line_name    = previous.get_line_name()
                        )
                    )
                    print(
                        'Switch over to {line_name}, heading towards {station_name}\n'
                        .format(
                            station_name = current.get_station2().get_name(),
                            line_name    = current.get_line_name()
                        )
                    )
                    
            previous = current
        pass