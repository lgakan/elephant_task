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

    def insert_edge_by_p_fun(self, start_vertex, end_vertex):
        start_vertex_pos = self.get_vertex_value(start_vertex)
        end_vertex_pos = self.get_vertex_value(end_vertex)
        self.neighborhood_list[start_vertex_pos] = end_vertex_pos

    def get_vertex_value(self, vertex):
        return self.vertex_dict[vertex]

    def __str__(self):
        answer = ""
        for i in range(len(self.neighborhood_list)):
            answer = answer + f"{i}: {self.neighborhood_list[i]} \n"
        return answer
