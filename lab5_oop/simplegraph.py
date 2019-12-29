class Vertex:
    def __init__(self, name='', edges=set()):
        self.name = name
        self.edges = edges

    def __repr__(self):
        return '{}, {}'.format(self.name, self.edges)

    def add_edge(self, edge):
        self.edges.add(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)


class Edge:
    def __init__(self, start, end, cost=1, visited=False):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = visited
        start.add_edge(self)

    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.start, self.end, self.cost, self.visited)


class SimpleGraph:
    def __init__(self, verts=set(), edges=set()):
        self.verts = verts
        self.edges = edges

    def add_vertex(self, v):
        self.verts += v

    def add_edge(self, v_1, v_2):
        self.edges += Edge(v_1, v_2)

    def contains_vertex(self, v):
        return v in self.verts

    def contains_edge(self, v_1, v_2):
        return Edge(v_1, v_2) in self.edges

    def get_neighbors(self, v):
        return [vertex for vertex in self.verts]

    def is_empty(self):
        return self.verts == set() and self.edges == set()

    def size(self):
        return len(self.verts)

    def remove_vertex(self, v):
        self.verts.remove(v)

    def remove_edge(self, v_1, v_2):
        self.edges.remove(Edge(v_1, v_2))

    def is_neighbor(self, v1, v2):
        return Edge(v1, v2) in self.edges

    def is_reachable(self, v1, v2):
        while



    def clear_all(self):
        self.verts = set()
        self.edges = set()

    def __repr__(self):
        return 'vertexs: {}'.format([vert.name for vert in self.verts])


a = Vertex('a')
b = Vertex('b')
c = Vertex('c')

my_verts = set([a, b])
e1 = Edge(a, b)
e2 = Edge(b, a)

my_edges = set([e1, e2])
graph = SimpleGraph(my_verts, my_edges)
empty_graph = SimpleGraph()

