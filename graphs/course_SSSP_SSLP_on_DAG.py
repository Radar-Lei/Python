#!/usr/bin/python

""" Author: Radar-Lei
    SSSP on DAG implementation for the lecture
    type of graph: weighted
    Side notes: the implementation is slightly different from the lecture-version.
    Instead of utilizing topsort results, this implementation is conducted based on BFS to update thd distance table
    greedily.
"""


class Graph:
    def __init__(self, nega_flag=False):
        self.adjList = {}  # To store graph: u -> (v,w)
        self.flag = nega_flag

    def add_edge(self, u, v, w):
        #  Edge going from node u to v and v to u with weight w
        # u (w)-> v, v (w) -> u
        if self.flag:
            w = -w
        # Check if u already in graph
        if u in self.adjList.keys():
            self.adjList[u].append((v, w))
        else:
            self.adjList[u] = [(v, w)]

    def show_graph(self):
        # u -> v(w)
        for u in self.adjList:
            print(u, "->", " -> ".join(str(f"{v}({w})") for v, w in self.adjList[u]))

    def dagShortestPath(self, start_node):
        dist = {key: None for key in self.adjList.keys()}  # init distance table
        dist[start_node] = 0

        # using bfs to solve
        queue = []
        queue.append(start_node)
        while len(queue) > 0:
            node = queue.pop(0)
            for each_tuple in self.adjList[node]:
                each_neighbor = each_tuple[0]
                if node != each_neighbor:
                    queue.append(each_neighbor)
                tmp_dist = each_tuple[1] + dist[node]
                if (dist[each_neighbor] == None) or (tmp_dist < dist[each_neighbor]):
                    dist[each_neighbor] = tmp_dist

        return dist

    def dagLongestPath(self, start_node):

        shortest_dist = self.dagShortestPath(start_node)
        for key, value in shortest_dist.items():
            shortest_dist[key] = -value
        return shortest_dist


if __name__ == "__main__":
    nega_flag = False
    g = Graph(nega_flag)  # False for SSSP on DAG, True for SSLP on DAG
    g.add_edge('A', 'B', 3)
    g.add_edge('A', 'C', 6)
    g.add_edge('B', 'C', 4)
    g.add_edge('B', 'D', 4)
    g.add_edge('B', 'E', 11)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'G', 11)
    g.add_edge('D', 'E', -4)
    g.add_edge('D', 'F', 5)
    g.add_edge('D', 'G', 2)
    g.add_edge('E', 'H', 9)
    g.add_edge('F', 'H', 1)
    g.add_edge('G', 'H', 2)
    g.add_edge('H', 'H', 0)
    g.show_graph()
    if not nega_flag:
        print('SSSP on DAG:')
        print(g.dagShortestPath('A'))
    else:
        print('SSLP on DAG:')
        print(g.dagLongestPath('A'))
