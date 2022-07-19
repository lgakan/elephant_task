import file_class
import graph_class



def main():
    file = file_class.FileReader("testowanko.txt")
    file_data = file.read_data_from_file()
    graph = graph_class.Graph()

    for i in range(1, file_data.el_number + 1):
        graph.insert_vertex(graph_class.Vertex(i))

    for i in range(1, file_data.el_number + 1):
        graph.insert_edge_by_p_fun(graph_class.Vertex(i), file_data.start_queue, file_data.end_queue)

    # print(graph)
    # print(graph.vertex_dict)
    # print(graph.neighborhood_list)
    # Rozklad p na cykle proste
    Cc = []
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
                x = graph_class.p_function(x + 1, file_data.start_queue, file_data.end_queue) - 1
            Cc.append(single_cycle)
    print(Cc)
    print(c)
    # Wyznaczenie parametrow cykli
    global_min = float("inf")
    cycles_min = []
    cycles_sum = []
    for i in range(c):
        sum_Ci = 0
        min_Ci = float("inf")
        for e in Cc[i]:
            sum_Ci += file_data.get_el_weight(e)
            min_Ci = min(min(file_data.get_cycle_weight(Cc[i])), file_data.get_el_weight(e))
        global_min = min(global_min, min_Ci)
        cycles_min.append(min_Ci)
        cycles_sum.append(sum_Ci)
    # Obliczenie wyniku
    w = 0
    for i in range(c):
        method_1 = cycles_sum[i] + (len(Cc[i]) - 2) * cycles_min[i]
        method_2 = cycles_sum[i] + cycles_min[i] + (len(Cc[i]) + 1) * global_min
        w += min(method_1, method_2)

    print(w)

if __name__ == "__main__":
    main()
