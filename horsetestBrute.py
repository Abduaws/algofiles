import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
import time

class problem:

    def __init__(self):
        self.graph = nx.DiGraph()
        self.board = dict()
        self.make_move_graph()
        self.pos = nx.spring_layout(self.graph)
        self.steps = 0

    def make_move_graph(self):
        self.graph.add_edge(1, 6)
        self.graph.add_edge(1, 8)
        self.graph.add_edge(2, 7)
        self.graph.add_edge(2, 9)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(3, 8)
        self.graph.add_edge(4, 3)
        self.graph.add_edge(4, 11)
        self.graph.add_edge(4, 9)
        self.graph.add_edge(5, 10)
        self.graph.add_edge(5, 12)
        self.graph.add_edge(6, 1)
        self.graph.add_edge(6, 7)
        self.graph.add_edge(6, 11)
        self.graph.add_edge(10, 5)
        self.graph.add_edge(10, 9)
        self.graph.add_edge(11, 4)
        self.graph.add_edge(11, 6)
        self.graph.add_edge(12, 7)
        self.graph.add_edge(12, 5)
        self.graph.add_edge(7, 6)
        self.graph.add_edge(7, 12)
        self.graph.add_edge(7, 2)
        self.graph.add_edge(8, 1)
        self.graph.add_edge(8, 3)
        self.graph.add_edge(9, 4)
        self.graph.add_edge(9, 10)
        self.graph.add_edge(9, 2)
        for node in list(self.graph.nodes):
            if node == 1 or node == 2 or node == 3:
                self.board[node] = "♞"
                continue
            elif node == 10 or node == 11 or node == 12:
                self.board[node] = "♘"
                continue
            self.board[node] = "-"

    def draw_graph(self):
        node_atrr = dict()
        for node in list(self.graph.nodes):
            if self.board[node] == "♞":
                node_atrr[node] = "♞"
            elif self.board[node] == "♘":
                node_atrr[node] = "♘"
            else:
                node_atrr[node] = "-"
        for node in list(self.graph.nodes):
            x, y = self.pos[node]
            plt.text(x, y + 0.07, s=node_atrr[node], color="black", fontsize= 24, zorder=20.0,
                     horizontalalignment='center')
        nx.draw_networkx(self.graph, pos=self.pos)
        plt.show()

    def get_adj(self, nodes, index):
        adj_node = [0]
        if nodes[index] == 1:
            adj_node[0] = 8
        elif nodes[index] == 2:
            adj_node[0] = 7
        elif nodes[index] == 3:
            adj_node[0] = 4
        elif nodes[index] == 4:
            adj_node[0] = 9
        elif nodes[index] == 5:
            adj_node[0] = 12
        elif nodes[index] == 7:
            adj_node[0] = 6
        elif nodes[index] == 8:
            adj_node[0] = 3
        elif nodes[index] == 10:
            adj_node[0] = 5
        elif nodes[index] == 11:
            adj_node[0] = 4
        elif nodes[index] == 12:
            adj_node[0] = 7
        elif nodes[index] == 9:
            adj_node[0] = 10
            adj_node.append(2)
        elif nodes[index] == 6:
            adj_node[0] = 1
            adj_node.append(11)
        return adj_node

    def solve_step_by_step(self):
        pass

    def solve(self):
        Flag = True
        while Flag:
            nodes = list(self.graph.nodes)
            horse_indexes = [index for index in range(0, len(nodes)) if self.board[nodes[index]] != "-"]
            if self.board[1] == "♘" and self.board[3] == "♘" and self.board[2] == "♘" and self.board[12] == "♞" and self.board[10] == "♞" and self.board[11] == "♞":
                print("Done")
                print(self.steps)
                return
            for index in horse_indexes:
                adj_node = self.get_adj(nodes, index)
                if self.board[nodes[index]] == "♞":
                    if nodes[index] == 11 or nodes[index] == 12:continue
                    if nodes[index] == 10 and self.board[12] == "♞":continue
                if self.board[nodes[index]] == "♘":
                    if nodes[index] == 2 or nodes[index] == 3: continue
                    if nodes[index] == 1 and self.board[3] == "♘": continue
                if len(adj_node) > 1:
                    node = int
                    if self.board[adj_node[1]] == "-":
                        if self.board[nodes[index]] == "♞" and adj_node[1] == 11: node = adj_node[1]
                        elif self.board[nodes[index]] == "♘" and adj_node[1] == 2: node = adj_node[1]
                    if node != adj_node[1]: node = adj_node[0]
                    if self.board[node] != "-": continue
                    print(f"{self.board[nodes[index]]}({nodes[index]} -> {node})")
                    self.board[node] = self.board[nodes[index]]
                    self.board[nodes[index]] = "-"
                    self.steps += 1
                    self.draw_graph()
                else:
                    if self.board[adj_node[0]] != "-": continue
                    print(f"{self.board[nodes[index]]}({nodes[index]} -> {adj_node[0]})")
                    self.board[adj_node[0]] = self.board[nodes[index]]
                    self.board[nodes[index]] = "-"
                    self.steps += 1
                    self.draw_graph()

threehorses = problem()
threehorses.draw_graph()
threehorses.solve()