import file_class
import graph_class


def p_function(start_value, start_queue, end_queue):
    for i in range(len(end_queue)):
        if end_queue[i] == start_value:
            return start_queue[i]


def solution():
    file_name = input()
    file = file_class.FileReader(file_name)
    file_data = file.read_data_from_file()
    graph = graph_class.Graph()

    for i in range(1, file_data.el_number + 1):
        graph.insert_vertex(graph_class.Vertex(i))

    for i in range(1, file_data.el_number + 1):
        start_vertex = graph_class.Vertex(i)
        p_value = p_function(i, file_data.start_queue, file_data.end_queue)
        end_vertex = graph_class.Vertex(p_value)
        graph.insert_edge_by_p_fun(start_vertex, end_vertex)

    # print(graph)
    # print(graph.vertex_dict)
    # print(graph.neighborhood_list)
    # Simple cycles
    C = []
    visited = [False] * file_data.el_number
    c = 0
    for i in range(file_data.el_number):
        if not visited[i]:
            single_cycle = []
            c += 1
            x = i
            while not visited[x]:
                visited[x] = True
                single_cycle.append(x)
                x = p_function(x + 1, file_data.start_queue, file_data.end_queue) - 1
            C.append(single_cycle)
    # cycle's parameters
    global_min = float("inf")
    cycles_min = []
    cycles_sum = []
    for i in range(c):
        sum_Ci = 0
        min_Ci = float("inf")
        for e in C[i]:
            sum_Ci += file_data.get_el_weight(e)
            min_Ci = min(min(file_data.get_cycle_weight(C[i])), file_data.get_el_weight(e))
        global_min = min(global_min, min_Ci)
        cycles_min.append(min_Ci)
        cycles_sum.append(sum_Ci)
    # Result
    answer = 0
    for i in range(c):
        method_1 = cycles_sum[i] + (len(C[i]) - 2) * cycles_min[i]
        method_2 = cycles_sum[i] + cycles_min[i] + (len(C[i]) + 1) * global_min
        answer += min(method_1, method_2)

    print(answer)


def main():
    solution()


if __name__ == "__main__":
    main()
