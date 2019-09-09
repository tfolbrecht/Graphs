"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        found = [starting_vertex]

        while queue.size() > 0:
            for vertex in self.vertices[queue.queue[0]]:
                if vertex not in found:
                    queue.enqueue(vertex)
                    found.append(vertex)
            queue.dequeue()
        print(f'BFT: {found}')

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        found = []

        while s.size() > 0:
            current = s.pop()
            if current not in found:
                found.append(current)
                for next_vert in self.vertices[current]:
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, path=[]):
        path += [starting_vertex]
        for vertex in self.vertices[starting_vertex]:
            if vertex not in path:
                path = self.dft_recursive(vertex, path)

        return path

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        found = []

        while queue.size() > 0:
            path = queue.dequeue()
            v = path[-1]

            if v not in found:
                if v == destination_vertex:
                    return path

                found.append(v)

                for next_vert in self.vertices[v]:

                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):

        stack = Stack()

        stack.push([starting_vertex])

        found = []

        while stack.size() > 0:
            path = stack.pop()
            v = path[-1]

            if v not in found:
                if v == destination_vertex:
                    return path
                found.append(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Graphs Vericies: " + str(graph.vertices))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT paths:" + str(graph.dft(1)))

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("BFT paths: " + str(graph.bft(1)))

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("DFT: " + str(graph.dft_recursive(1)))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS: " + str(graph.bfs(1, 6)))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS: " + str(graph.dfs(1, 6)))
