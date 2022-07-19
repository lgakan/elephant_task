import sys
from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class FileData:
    el_number: int
    el_weight: list
    start_queue: list
    end_queue: list

    def get_el_weight(self, number):
        return self.el_weight[number]

    def get_cycle_weight(self, cycles):
        answer = []
        for i in cycles:
            answer.append(self.el_weight[i])
        return answer

    def __str__(self):
        return f"el_number = {self.el_number}\nel_weight= {self.el_weight}\nstart_queue = {self.start_queue}\nend_queue = {self.end_queue} "


class FileReader:
    def __init__(self, path):
        self.path = self.set_path(path)


    def set_path(self, path):
        try:
            open(path, 'r')
        except OSError as e:
            print(f"Unable to open {path}: {e}", file=sys.stderr)
        return path

    def read_data_from_file(self):
        el_number = None
        el_weight = None
        start_queue = None
        end_queue = None
        with open(self.path, "r") as file:
            for line_idx, line in enumerate(file):
                line = line.strip('\n')
                line_value = list(map(int, line.split()))
                match line_idx:
                    case 0:
                        el_number = line_value[0]
                    case 1:
                        el_weight = line_value
                    case 2:
                        start_queue = line_value
                    case 3:
                        end_queue = line_value
        return FileData(el_number=el_number, el_weight=el_weight, start_queue=start_queue, end_queue=end_queue)
