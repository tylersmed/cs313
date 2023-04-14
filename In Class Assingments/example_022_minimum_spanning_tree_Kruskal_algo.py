class Graph:
# A simple representation of a weighted graph

    def __init__(self, no_vertices):
        self.no_vertices = no_vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # A Search function
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A Simple union Function 
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []
        
        for node in range(self.no_vertices):
            parent.append(node)
            rank.append(0)

        connected_nodes = []
        for x, y, _ in self.edges:
            if x not in connected_nodes:
                connected_nodes.append(x)
            if y not in connected_nodes:
                connected_nodes.append(y)

        while e < len(connected_nodes)-1: #self.no_vertices - 1:
            u, v, w = self.edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        
        tot_weight = 0
        for u, v, weight in result:
            # print("%d - %d: %d" % (u, v, weight))
            tot_weight += weight
        return tot_weight, result
  
def main():
  # create the Graph object
    # graph 1 test
    """
    graph1 = Graph(8)
    graph1.add_edge(0, 1, 2)
    graph1.add_edge(0, 2, 5)
    graph1.add_edge(1, 3, 6)
    graph1.add_edge(1, 5, 2)
    graph1.add_edge(2, 6, 1)
    graph1.add_edge(3, 5, 4)
    graph1.add_edge(4, 6, 1)
    graph1.add_edge(5, 6, 6)
    graph1.add_edge(6, 7, 3)

    print(graph1.edges)
    print(graph1.kruskal_algo())
    """

    # disconnected graph test
    discnctd_graph = Graph(6)
    discnctd_graph.add_edge(0, 2, 5)
    discnctd_graph.add_edge(0, 3, 5)
    discnctd_graph.add_edge(0, 4, 5)
    discnctd_graph.add_edge(3, 5, 9)

    print(discnctd_graph.edges)
    print(discnctd_graph.kruskal_algo())
  

#   print(g1.edges)
#   g1.kruskal_algo()


if __name__ == "__main__":
  main()
