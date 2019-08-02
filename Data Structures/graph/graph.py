import math
vertices = list()


class Node:
    def __init__(self):
        global vertices
        vertices.append(self)
        self.data = None
        self.neighbour = list()
        self.distance = math.inf

    def add_data(self, d):
        self.data = d

    def add_neighbour(self, a, w, s):
        e = Edge()
        e.make_edge(a, w, s)
        connect = False
        for i in self.neighbour:
            if i.connected_to == a:
                connect = True
        if not connect:
            self.neighbour.append(e)


class Graph:
    vertices = list()

    def add_edge(self, a, b, w, s):
        if s == 'single':
            a.add_neighbour(b, w, s)
        else:
            a.add_neighbour(b, w, s)
            b.add_neighbour(a, w, s)

    def delete_node(self, a):
        for i in a.neighbour:
            i.neighbour.remove(a)


class Edge:
    def __init__(self):
        self.connected_to = None
        self.weight = None
        self.direction = None

    def make_edge(self, a, w, s):
        self.connected_to = a
        self.weight = w
        self.direction = s


g = Graph()
a = Node()
b = Node()
c = Node()
d = Node()
b.add_data(18)
a.add_data(5)
c.add_data(34)
d.add_data(8)
g.add_edge(a, b, 4, 'double')
g.add_edge(c, a, 5, 'double')
g.add_edge(c, d, 6, 'double')
g.add_edge(d, b, 7, 'double')
for i in vertices:
    print(i.data)
print(a.neighbour)
def dj(a):
    a.distance = 0
    vertices.remove(a)
    current = a
    current_weights = list()
    current_nodes = list()
    current_neighbour = list()
    while len(vertices) > 0:
        for j in range(len(current_neighbour)):
        for i in current.neighbour:
            current_neighbour.append(i)
            current_weights.append(i.weight)
            current_nodes.append(i.connected_to)
        mini = min(current_weights)
        ind = current_weights.index(mini)
        node = current_neighbour[ind]
        next  = current_nodes[ind]
        indices = current_neighbour.index(node)
        w = current_neighbour[indices]
        if current.distance + w.weight < next.distance:
            next.distance = current.distance + w.weight

dj(a)