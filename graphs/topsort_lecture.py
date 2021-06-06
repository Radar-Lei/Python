#!/usr/bin/python

""" Author: Radar-Lei
    topological sort implementation for the lecture
"""


class Graph:
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertices
    def print_graph(self) -> None:
        print(self.vertex)

    # for adding the edge between two vertices
    def add_edge(self, from_vertex: str, to_vertex: str) -> None:
        # check if vertex is already present,
        if from_vertex in self.vertex:
            self.vertex[from_vertex].append(to_vertex)
        else:
            # else make a new vertex
            self.vertex[from_vertex] = [to_vertex]

    def topsort(self):

        N = len(self.vertex)
        V = {key: False for key in self.vertex.keys()}
        ordering = [0] * N
        i = N - 1

        for at in self.vertex.keys():
            if V[at] == False:
                i = self.dfs(i, at, V, ordering)

        return ordering

    def dfs(self, i, at, V, ordering):
        V[at] = True

        for each in self.vertex[at]:
            if (each == at) and V[each] == False: # dead end
                V[each] = True
                ordering[i] = each
                i -= 1
            elif (each in V.keys()) and (V[each] == False):
                i = self.dfs(i, each, V, ordering)
        ordering[i] = at
        return i - 1

if __name__ == "__main__":
    g = Graph()
    g.add_edge('C', 'B')
    g.add_edge('C', 'A')
    g.add_edge('A', 'D')
    g.add_edge('B', 'D')
    g.add_edge('D', 'G')
    g.add_edge('D', 'H')
    g.add_edge('E', 'A')
    g.add_edge('E', 'D')
    g.add_edge('E', 'F')
    g.add_edge('G', 'I')
    g.add_edge('H', 'I')
    g.add_edge('H', 'J')
    g.add_edge('I', 'L')
    g.add_edge('J', 'L')
    g.add_edge('F', 'K')
    g.add_edge('F', 'J')
    g.add_edge('K', 'J')
    g.add_edge('J', 'M')
    #create slef link for dead ends
    g.add_edge('M', 'M')
    g.add_edge('L', 'L')

    g.print_graph()
    print("Ordering:")
    print(g.topsort())
