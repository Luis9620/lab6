from disjoint_set_forest import DisjointSetForest
#MST = spanning tree with weight less than or equal to the weight of
# every other spanning tree.
def kruskal_algorithm(graph):       #Method for finding the MST
    edges = []

    for vertex in range(graph.get_num_vertices()):
        for adj_vertex in graph.get_vertices_reachable_from(vertex):
            edges.append([graph.get_edge_weight(vertex, adj_vertex), adj_vertex, vertex])

    edges.sort()
    dsf = DisjointSetForest(graph.get_num_vertices())
    T = []

    for i in range(len(edges)):
        src = edges[i][2]
        dest = edges[i][1]
        if creates_cycle(dsf,src,dest) == False:
            T.append(edges[i])
            dsf.union(edges[i][2] , edges[i][1])

    for i in range(len(T)):
        T[i].reverse()

    return T


def creates_cycle(dsf, src, dest):
        if dsf.find(src) == dsf.find(dest):
            return True
        return False