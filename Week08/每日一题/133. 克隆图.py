# 133. 克隆图.py


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors


class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


# 以下为自我练习
class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val)
        self.visited[node] = clone_node
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return clone_node


def main():
    pass


if __name__ == '__main__':
    main()
