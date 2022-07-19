class Vertex:
    def __init__(self, pos):
        self.pos = pos

    def __eq__(self, other):
        if self.pos == other.pos:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.pos)


def list_2_dict(v_list) -> dict:
    returned_dict = dict()
    for i in range(len(v_list)):
        returned_dict[v_list[i]] = i

    return returned_dict


def p_function(start_value, start_queue, end_queue):
    for i in range(len(end_queue)):
        if end_queue[i] == start_value:
            return start_queue[i]
#
#
# def get_el_weight(el_number, el_weight):
#     return el_weight[el_number]
#
#
# def get_cycle_weight(el_numbers, el_weight):
#     answer = []
#     for i in el_numbers:
#         answer.append(el_weight[i])
#     return answer


class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.neighborhood_list = []

    def insert_vertex(self, vertex):
        old_size = len(self.vertex_dict)
        self.vertex_dict[vertex] = len(self.vertex_dict)
        new_size = len(self.vertex_dict)

        if new_size > old_size:
            self.neighborhood_list.append(None)

    def insert_edge_by_p_fun(self, vertex, start_queue, end_queue):
        vertex_value_i = self.get_vertex_value(vertex)
        vertex_value_j = p_function(vertex.pos, start_queue, end_queue)
        self.neighborhood_list[vertex_value_i] = vertex_value_j

    def get_vertex_value(self, vertex):
        return self.vertex_dict[vertex]

    def size(self):
        answer = 0
        for i in self.neighborhood_list:
            answer += len(i)
        return answer

    def neighbours(self, vertex_idx):
        answer = []
        found_neighbor = None
        for i in range(len(self.vertex_dict)):
            check = list(self.vertex_dict.items())
            if check[i][1] == vertex_idx:
                found_neighbor = self.neighborhood_list[i]
                break

        if found_neighbor is None:
            return None

        for i in range(len(found_neighbor)):
            previous = found_neighbor[i]
            answer.append(previous)
        return answer

    def __str__(self):
        answer = ""

        for i in range(len(self.neighborhood_list)):
            answer = answer + f"{i}: {self.neighborhood_list[i]} \n"
        return answer