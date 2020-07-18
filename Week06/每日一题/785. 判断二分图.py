# 785. 判断二分图.py
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(n, color, visited):
            # recursion terminator
            if n in visited:
                if visited[n] == color:
                    return False
                return
            # process current level logic
            visited[n] = color
            for next_n in graph[n]:
                # drill down
                if not dfs(next_n, not color, visited):
                    return False
            return True

        visited = {}
        for i in range(len(graph)):
            if i not in visited:
                if not dfs(i, True, visited):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = not color[pos]
                    if not dfs(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                if not dfs(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(pos):
            # recursion terminator
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                # process current level logic
                else:
                    color[i] = 1 - color[pos]
                    # drill down
                    if not dfs(i):
                        # merge
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                # 这里注意，新来的可以一定可以随便染色，因为图是无向的，
                # 我们使用的是dfs，必然它链接的点也没被访问过
                color[i] = 0
                if not dfs(i):
                    return False
        return True


def main():
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    sol = Solution()
    res = sol.isBipartite(graph)
    print(res)


if __name__ == '__main__':
    main()
