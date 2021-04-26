class Vertex:
    def __init__(self, node_id):
        self.id = node_id
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node_id):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node_id)
        self.vert_dict[node_id] = new_vertex
        return new_vertex

    def get_vertex(self, node_id):
        if node_id in self.vert_dict:
            return self.vert_dict[node_id]
        else:
            return None

    def add_edge(self, frm_id, to_id, cost=0):
        if frm_id not in self.vert_dict:
            self.add_vertex(frm_id)
        if to_id not in self.vert_dict:
            self.add_vertex(to_id)

        self.vert_dict[frm_id].add_neighbor(self.vert_dict[to_id], cost)
        self.vert_dict[to_id].add_neighbor(self.vert_dict[frm_id], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print(f'( {vid} , {wid}, {v.get_weight(w)})')

    for v in g:
        print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))