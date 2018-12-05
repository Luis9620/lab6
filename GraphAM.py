class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        self.dsf[a] = self.find(self.dsf[a])

        return self.dsf[a]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.dsf[rb] = ra

    def get_num_of_sets(self):
        count = 0

        for num in self.dsf:
            if num < 0:
                count += 1

        return count


class GraphAM:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_matrix = []

        for i in range(initial_num_vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.adj_matrix.append([0] * initial_num_vertices)

        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_matrix)

    def add_vertex(self):
        for lst in self.adj_matrix:
            lst.append(0)

        new_row = [0] * (len(self.adj_matrix) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.adj_matrix.append(new_row)

        return len(self.adj_matrix) - 1  # Return new vertex id

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.adj_matrix[src][dest] = weight

        if not self.is_directed:
            self.adj_matrix[dest][src] = weight

    def remove_edge(self, src, dest):
        self.add_edge(src,dest, 0)

    def get_num_vertices(self):
        return len(self.adj_matrix)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[i][dest] != 0:
                vertices.add(i)

        return vertices

    def __str__(self):

        return str(self.adj_matrix)


# ---------------------------------------------------------------------------------------
# --------------------------- Problem 6 ---------------------------
# ---------------------------------------------------------------------------------------
    def get_vertex_in_degree(self, v):
        if not self.is_valid_vertex(v):
            return

        in_degree_count = 0

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[i][v] != 0:
                in_degree_count += 1

        return in_degree_count

# ---------------------------------------------------------------------------------------
# --------------------------- Problem 7 ---------------------------
# ---------------------------------------------------------------------------------------
    def is_there_a_2_vertex_cycle(self):

        for src in range(len(self.adj_matrix)):
            for dest in range(src + 1, len(self.adj_matrix)):
                if self.adj_matrix[src][dest] != 0 and self.adj_matrix[dest][src] != 0:
                    return True

        return False


# ---------------------------------------------------------------------------------------
# --------------------------- Problem 8 ---------------------------
# ---------------------------------------------------------------------------------------
    def get_num_connected_components(self):

        dsf = DisjointSetForest(len(self.adj_matrix))

        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if self.adj_matrix[i][j] != 0:
                    dsf.union(i, j)

        return dsf.get_num_of_sets()


    # ---------------------------------------------------------------------------------------
    # --------------------------- Problem 9 ---------------------------
    # ---------------------------------------------------------------------------------------
    def create_circle_graph(self, n):

        if n < 2:  # Assumption -> n should be at least 2
            return

        # Create empty graph
        self.adj_matrix = []

        for i in range(n):  # Assumption / Design Decision: 0 represents non-existing edge
            self.adj_matrix.append([0] * n)

        self.is_directed = True

        # Add edges
        for i in range(n - 1):
            self.adj_matrix[i][i + 1] = 1.0

        self.adj_matrix[n - 1][0] = 1.0

        # Another way of doing the same thing:

        # for i in range(n):
        #     self.adj_matrix.append[i][ (i + 1) % n] = 1.0

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P3 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_highest_cost_edge(self):

        highest_cost_edge = -float('inf')

        for src in range(len(self.adj_matrix)):
            for dest in range(len(self.adj_matrix)):
                highest_cost_edge = max(self.adj_matrix[src][dest], highest_cost_edge)

        return highest_cost_edge


    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P4 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_num_edges(self):

        num_edges = 0

        for src in range(len(self.adj_matrix)):
            for dest in range(len(self.adj_matrix)):
                if self.adj_matrix[src][dest] != 0:
                    num_edges += 1

        return num_edges


    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P5 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_edge_weight(self, src, dest):

        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        return self.adj_matrix[src][dest]

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P6 ---------------------------
    # ---------------------------------------------------------------------------------------
    def reverse_edges(self):
        new_adj_matrix = []

        for i in range(len(self.adj_matrix)):  # Assumption / Design Decision: 0 represents non-existing edge
            new_adj_matrix.append([0] * len(self.adj_matrix))

        for src in range(len(self.adj_matrix)):
            for dest in range(len(self.adj_matrix)):
                if self.adj_matrix[src][dest] != 0:
                    new_adj_matrix[dest][src] = self.adj_matrix[src][dest]

        self.adj_matrix = new_adj_matrix

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P7 ---------------------------
    # ---------------------------------------------------------------------------------------
    def is_identical(self, graph):

        if len(self.adj_matrix) != len(graph.adj_matrix):
            return False

        for src in range(len(self.adj_matrix)):
            for dest in range(len(self.adj_matrix)):
                if self.adj_matrix[src][dest] != graph.adj_matrix[src][dest]:
                    return False

        return True

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P8 ---------------------------
    # ---------------------------------------------------------------------------------------
    def is_self_edge(self, v):
        if not self.is_valid_vertex(v):
            return False

        return self.adj_matrix[v][v] != 0

    def get_num_of_self_edges(self):

        num_self_edges = 0

        for u in range(len(self.adj_matrix)):
            if self.is_self_edge(u):
                num_self_edges += 1

        return num_self_edges

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P9 ---------------------------
    # ---------------------------------------------------------------------------------------
    def get_complement(self):
        complement = GraphAM(len(self.adj_matrix), self.is_directed)

        for src in range(len(self.adj_matrix)):
            for dest in range(len(self.adj_matrix)):
                if src != dest and self.adj_matrix[src][dest] == 0:
                    complement.adj_matrix[src][dest] = 1.0

        return complement


    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P10 ---------------------------
    # ---------------------------------------------------------------------------------------
    def is_subgraph(self, g1):  # g1 is a graph represented using an adjacency list

        if len(g1.adj_list) > len(self.adj_matrix):
            return False

        for i in range(len(g1.adj_list)):
            temp = g1.adj_list[i]

            while temp is not None:
                if self.adj_matrix[i][temp.item] == 0:
                    return False

                temp = temp.next

        return True

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P11 ---------------------------
    # ---------------------------------------------------------------------------------------
    def contains_cycle(self):  # Assumption: Undirected

        dsf = DisjointSetForest(len(self.adj_matrix))

        for src in range(len(self.adj_matrix)):
            for dest in range(len(self.adj_matrix)):
                if self.adj_matrix[src][dest] != 0:
                    if dsf.find(src) == dsf.find(dest):
                        return True

                    dsf.union(src, dest)

        return False

    # ---------------------------------------------------------------------------------------
    # --------------------------- Exercise P12 ---------------------------
    # ---------------------------------------------------------------------------------------
    def is_isolated(self, v):
        if not self.is_valid_vertex(v):
            return False

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[i][v] != 0 or self.adj_matrix[v][i] != 0:
                return False

        return True
