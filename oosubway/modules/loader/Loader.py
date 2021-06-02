from io import TextIOWrapper

from ..subway import Subway

class Loader():
    def __init__(self):
        return None
    
    def load_from_file(self, file_path: str)->Subway:
        subway = Subway()

        fp = open(file_path, 'r')

        # create stations
        self.load_stations(subway, fp)

        # create lines(connections)
        line_name = fp.readline()
        while len(line_name.strip()) > 0:
            self.load_lines(subway, line_name, fp)
            line_name = fp.readline()

        fp.close()

        return subway
    
    def load_stations(self, subway: Subway, fp: TextIOWrapper)->None:
        line = fp.readline()

        while len(line.strip()) > 0:
            subway.add_station(line)
            line = fp.readline()

        return None
    
    def load_lines(self, subway: Subway, line_name: str, fp: TextIOWrapper)->None:
        pre_station = ''
        cur_station = fp.readline()

        while len(cur_station.strip()) > 0:
            if len(pre_station) > 0:
                subway.add_connection(pre_station, cur_station, line_name)
            
            pre_station = cur_station
            cur_station = fp.readline()

        return None
