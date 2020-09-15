# tarjan_scc.py
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def scc_util(self, u, low, disc, stack_member, stack: list):
        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stack_member[u] = True
        stack.append(u)

        # Go through all vertices adjacent to this
        for v in self.graph[u]:
            # If v is not visited yet, then recur for it
            if disc[v] == -1:
                self.scc_util(v, low, disc, stack_member, stack)
                # check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])
            elif stack_member[v]:
                # Update low value of 'u' only if 'v' is still in stack
                # (i.e. it's a back edge, not cross edge).
                # Case 2 (per above discussion on Disc and Low value)
                low[u] = min(low[u], disc[v])
        # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = stack.pop()
                print(w, end=' ')
                stack_member[w] = False
            print()

    # The function to do DFS traversal
    # It uses recursive SCCUtil()1
    def scc(self):
        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * self.V
        low = [-1] * self.V
        stack_member = [False] * self.V
        stack = []
        for i in range(self.V):
            if disc[i] == -1:
                self.scc_util(i, low, disc, stack_member, stack)


# 以下为自我练习
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.neigh = defaultdict(list)
        self.Time = 0

    def addEdge(self, x, y):
        self.neigh[x].append(y)

    def scc(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if disc[i] == -1:
                self.scc_util(i, low, disc, visited, stack)

    def scc_util(self, u, low, disc, visited, stack):
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        visited[u] = True
        stack.append(u)
        for v in self.neigh[u]:
            if disc[v] == -1:
                self.scc_util(v, low, disc, visited, stack)
                low[u] = min(low[u], low[v])
            elif visited[v]:
                low[u] = min(low[u], disc[v])
        w = -1
        if disc[u] == low[u]:
            while w != u:
                w = stack.pop()
                print(w, end=' ')
                visited[w] = False
            print()


def main():
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    print("SCC in first graph")
    g1.scc()

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print("SCC in second graph")
    g2.scc()

    g3 = Graph(7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    print("SCC in third graph")
    g3.scc()

    g4 = Graph(11)
    g4.addEdge(0, 1)
    g4.addEdge(0, 3)
    g4.addEdge(1, 2)
    g4.addEdge(1, 4)
    g4.addEdge(2, 0)
    g4.addEdge(2, 6)
    g4.addEdge(3, 2)
    g4.addEdge(4, 5)
    g4.addEdge(4, 6)
    g4.addEdge(5, 6)
    g4.addEdge(5, 7)
    g4.addEdge(5, 7)
    g4.addEdge(5, 8)
    g4.addEdge(5, 9)
    g4.addEdge(6, 4)
    g4.addEdge(7, 9)
    g4.addEdge(8, 9)
    g4.addEdge(9, 8)
    print("SCC in forth graph")
    g4.scc()

    g5 = Graph(5)
    g5.addEdge(0, 1)
    g5.addEdge(1, 2)
    g5.addEdge(2, 3)
    g5.addEdge(2, 4)
    g5.addEdge(3, 0)
    g5.addEdge(4, 2)
    print("SCC in fifth graph")
    g5.scc()


if __name__ == '__main__':
    main()
