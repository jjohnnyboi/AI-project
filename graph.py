# Node of the graph
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = {}
        self.visited = False

    # add a neighbour name to a vertex
    def add_neighbor(self, vertexName, cost):
        if vertexName not in self.neighbors:
            self.neighbors[vertexName] = cost


class Graph:
    # Dictionary  of Vertices in the graph =>key = vertex name, value = object of vertex
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    # Create edge between two vertices that already exists in the graph
    def add_edge(self, vertex1, vertex2, cost):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # key = vertex name, value = object of vertex
            for key, value in self.vertices.items():
                # Adding each vertex name neighbour to the other vertex with cost
                if key == vertex1:
                    value.add_neighbor(vertex2, cost)
                if key == vertex2:
                    value.add_neighbor(vertex1, cost)
            return True
        else:
            return False

    # Print each vertex and its neighbours in graph
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
