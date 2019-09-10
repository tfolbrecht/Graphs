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
    graph.dfs()