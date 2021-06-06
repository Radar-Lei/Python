#!/usr/bin/python

""" Author: Radar-Lei undirected version and applied to connected components identification"""


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

    def findComponents(self):

        # visited array for storing already visited nodes
        visited = [False] * len(self.vertex)

        # call the recursive helper function
        for i in range(len(self.vertex)):
            if not visited[i]:
                self.dfs_recursive(i, visited)
                self.count += 1
        return self.count, self.components

    def dfs_recursive(self, start_vertex: int, visited: list) -> None:
        # mark start vertex as visited
        visited[start_vertex] = True
        self.components.append(self.count)

        print(start_vertex, end=" ")

        # Recur for all the vertices that are adjacent to this node
        for i in self.vertex[start_vertex]:
            if not visited[i]:
                self.dfs_recursive(i, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 4)
    g.add_edge(0, 8)
    g.add_edge(0, 14)
    g.add_edge(0, 13)
    g.add_edge(8, 4)
    g.add_edge(8, 14)
    g.add_edge(13, 14)
    g.add_edge(15, 10)
    g.add_edge(15, 2)
    g.add_edge(15, 9)
    g.add_edge(9, 2)
    g.add_edge(9, 3)
    g.add_edge(5, 1)
    g.add_edge(5, 16)
    g.add_edge(5, 17)
    g.add_edge(6, 11)
    g.add_edge(11,7)
    g.add_edge(7, 6)
    g.add_edge(12, 12)

    g.print_graph()
    print("DFS:")
    count, components = g.findComponents()
    print(count)
    print(components)

    # OUTPUT:
    # 0  ->  1 -> 2
    # 1  ->  2
    # 2  ->  0 -> 3
    # 3  ->  3
    # DFS:
    #  0 1 2 3
