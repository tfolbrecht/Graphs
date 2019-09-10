from util import Graph, Queue


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # vertex relation read as tuples
    # util.py 31
    for tups in ancestors:
        graph.add_vertex(tups[0])
        graph.add_vertex(tups[1])
        graph.add_edge(tups[0], tups[1])
        print(graph.vertices)
    # print(graph.vertices)

    q = Queue()
    longest_list = 0
    furthest_ancestor = -1
    for parent in graph.vertices:
        q.enqueue([parent])
        found = []
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in found:
                if v == starting_node:
                    if len(path) > longest_list:
                        longest_list = len(path)
                        furthest_ancestor = parent
                    else:
                        break
                found.append(v)
                for next_vert in graph.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
    if furthest_ancestor == starting_node:
        furthest_ancestor = -1
    print(furthest_ancestor)
    return furthest_ancestor
