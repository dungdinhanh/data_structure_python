import stack
import queue

class Vertex:
    def __init__(self, data=None):
        self.data = data
        self.adjacent_vertices = []
        self.list_edge = []

    def add_edge(self, other, weight=None, un_dir=False):
        if type(other) != type(self):
            return
        edge = Edge()
        for temp in self.adjacent_vertices:
            if temp.data == other.data:
                return
        edge.connect(self, other, weight)
        self.list_edge.append(edge)
        self.adjacent_vertices.append(other)
        if un_dir:
            new_edge = Edge()
            new_edge.connect(other, self, weight)

    def check_adjacent(self, other):
        if type(other) != type(self):
            return False
        for element in self.adjacent_vertices:
            if element.data == other.data:
                return True
        return False

    def get_adjacency(self):
        return self.adjacent_vertices

    def get_edges(self):
        return self.list_edge

    def delete_edge(self, vertex):
        for edge in self.list_edge:
            if edge.second_vertex.data == vertex.data:
                self.list_edge.remove(edge)

    def __str__(self):
        return self.data

class Edge:
    def __init__(self, first_vertex=None, second_vertex=None, weight=None):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.weight = weight

    def connect(self, first_vertex, second_vertex, weight=None):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        if weight is None:
            self.weight = 1
        else:
            self.weight = weight


class Graph:
    def __init__(self):
        self.vertices = []

    def get_adjacency(self, data):
        for vertex in self.vertices:
            if vertex.data == data:
                return vertex.get_adjacency()

    def add_vertex(self, data):
        new_vertex = Vertex(data=data)
        for temp in self.vertices:
            if temp.data == data:
                return None
        self.vertices.append(new_vertex)

    def find_vertex(self, data):
        for temp in self.vertices:
            if temp.data == data:
                return temp

    def add_edge(self, data1, data2, weight=1, un_dir=True):
        vertex1 = self.find_vertex(data1)
        vertex2 = self.find_vertex(data2)
        vertex1.add_edge(vertex2, weight=weight, un_dir=un_dir)

    def s



graph = Graph()
graph.add_edge(5)
graph.add_vertex(6)
list_vertex = graph.vertices
print(list_vertex)




