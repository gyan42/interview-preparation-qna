"""
A Python program to demonstrate the adjacency
list representation of the graph
"""


# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph_list = [None] * self.num_vertices

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph_list[src]
        self.graph_list[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph_list[dest]
        self.graph_list[dest] = node

    # Function to print the graph
    def print_graph(self):
        print("Adjacency list of vertex")
        for i in range(self.num_vertices):
            print("node({})".format(i, i), end="")
            temp = self.graph_list[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


        # Driver program to the above graph class
if __name__ == "__main__":
    graph = Graph(num_vertices=5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)

    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    graph.add_edge(2, 3)

    graph.add_edge(3, 4)

    graph.print_graph()

"""
Adjacency list of vertex
node(0) -> 4 -> 1 

node(1) -> 4 -> 3 -> 2 -> 0 

node(2) -> 3 -> 1 

node(3) -> 4 -> 2 -> 1 

node(4) -> 3 -> 1 -> 0 
"""