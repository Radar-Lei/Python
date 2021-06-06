"""Breadth-first search shortest path implementation on a grid.
    Manual test:
    python
"""
import numpy as np


class grid_bfs:
    def __init__(self):
        # create obstacle matrix
        self.m = np.array([['.', '.', '.', '#', '.', '.', '.'],
                           ['.', '#', '.', '.', '.', '#', '.'],
                           ['.', '#', '.', '.', '.', '.', '.'],
                           ['.', '.', '#', '#', '.', '.', '.'],
                           ['#', '.', '#', '.', '.', '#', '.']])
        # replace notations of start and end nodes
        self.m[0][0] = 'S'
        self.m[4][3] = 'E'
        self.R, self.C = self.m.shape[0], self.m.shape[1]
        # starting node index
        self.sr, self.sc = 0, 0
        self.rq = []
        self.cq = []
        self.move_count = 0
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0

        self.reached_end = False

        self.visited = np.zeros(self.m.shape)

        self.dr = [-1, 1, 0, 0]
        self.dc = [0, 0, 1, -1]

    def solve(self):

        self.rq.append(self.sr)
        self.cq.append(self.sc)

        self.visited[self.sr][self.sc] = 1

        while len(self.rq) > 0:
            r = self.rq.pop(0)
            c = self.cq.pop(0)
            if self.m[r][c] == 'E':
                self.reached_end = True
                break
            self.explore_neighbors(r, c)
            self.nodes_left_in_layer -= 1
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                self.move_count += 1
        if self.reached_end:
            return self.move_count
        return -1

    def explore_neighbors(self, r, c) -> None:
        for i in range(len(self.dr)):
            rr = r + self.dr[i]
            cc = c + self.dc[i]

            if rr < 0 or cc < 0:
                continue
            elif rr >= self.R or cc >= self.C:
                continue

            if self.visited[rr][cc]:
                continue
            elif self.m[rr][cc] == '#':
                continue

            self.rq.append(rr)
            self.cq.append(cc)
            self.visited[rr][cc] = 1
            self.nodes_in_next_layer += 1



if __name__ == "__main__":
    g = grid_bfs()
    print(g.solve())