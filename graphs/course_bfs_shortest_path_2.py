"""Breadth-first search shortest path implementation for the lecture.
    Manual test: for undirected unweighted graphs
    python bfs_shortest_path.py
"""

class Graph:
    def __init__(self):
        self.vertex = {}
        self.count = 0
        self.components = []

    # for printing the Graph vertices
    def print_graph(self) -> None:
        print(self.vertex)


    # for adding the edge between two vertices
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        # check if vertex is already present,
        if from_vertex in self.vertex and to_vertex not in self.vertex:
            self.vertex[from_vertex].append(to_vertex)
            self.vertex[to_vertex] = [from_vertex]
        elif from_vertex not in self.vertex and to_vertex in self.vertex:
            self.vertex[to_vertex].append(from_vertex)
            self.vertex[from_vertex] = [to_vertex]
        elif from_vertex in self.vertex and to_vertex in self.vertex:
            self.vertex[from_vertex].append(to_vertex)
            self.vertex[to_vertex].append(from_vertex)
        else:
            # else make a new vertex
            self.vertex[from_vertex] = [to_vertex]
            self.vertex[to_vertex] = [from_vertex]

    def solve(self, s):
        queue = []
        queue.append(s)

        visited = [False] * len(self.vertex)
        visited[s] = True
        # prev tracks the node id of the previous node for the vertex at the current list position
        #e.g. prev[9], prev[7] and prev[11] will all be 0.
        #if there exists a single-node disjunctive component, that prev[that node] = None
        # this is useful since if that disconnected node happens to be either the start node or end node
        # we can output that it's possible for us to find a shortest path in that scenario
        prev = [None] * len(self.vertex)
        while len(queue) > 0:
            node = queue.pop(0)
            for each_nei in self.vertex[node]:
                if not visited[each_nei]:
                    queue.append(each_nei)
                    visited[each_nei] = True
                    prev[each_nei] = node
        return prev

    def reconstructPath(self, s, e, prev):

        path = []
        at = e
        while at is not None:
            path.append(at)
            at = prev[at]

        path.reverse()

        if path[0] == s:
            return path
        return []

    def bfs(self, s, e):

        prev = self.solve(s)

        return self.reconstructPath(s, e, prev)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 9)
    g.add_edge(0, 7)
    g.add_edge(0, 11)
    g.add_edge(9, 10)
    g.add_edge(9, 8)
    g.add_edge(7, 3)
    g.add_edge(7, 6)
    g.add_edge(7, 11)
    g.add_edge(10, 1)
    g.add_edge(8, 1)
    g.add_edge(8, 12)
    g.add_edge(6, 5)
    g.add_edge(3, 4)
    g.add_edge(3, 2)
    g.add_edge(12, 2)

    g.print_graph()
    print(g.bfs(0,2))

