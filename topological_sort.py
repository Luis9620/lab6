from queue import Queue
#A topological sort is an ordeing of the vertices in a
#directed acyclic graph such that if there is a path from u to v,
#v appearrs after u in the ordering
def topological_sort(graph):
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = []
    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:      #Adding to the queue the vertex with indegree of 0
            q.put(i)

    while not q.empty():
        u = q.get()  #Dequeue
        sort_result.append(u)

        for adj_vertex in graph.get_vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1
            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)

    if len(sort_result) != graph.get_num_vertices():  #Cycle found
        return None

    return sort_result


def compute_indegree_every_vertex(graph): #Method for computing the indegree of every vertex
    indegrees = []

    for i in range(graph.get_num_vertices()):
        indegrees.append(len(graph.get_vertices_that_point_to(i)))

    return indegrees