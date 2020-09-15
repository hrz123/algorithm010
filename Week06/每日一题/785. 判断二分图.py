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
            # process current row logic
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
                # process current row logic
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


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def coloring(pos):
            for i in graph[pos]:
                if i in color:
                    # 在不能是相同颜色
                    if color[i] == color[pos]:
                        return False
                else:
                    # 不在要染成不同颜色
                    color[i] = not color[pos]
                    if not coloring(i):
                        return False
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                if not coloring(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
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

        def bfs(i):
            q, nq = [i], []
            while q:
                for v in q:
                    for nv in graph[v]:
                        if nv in color:
                            if color[nv] == color[v]:
                                return False
                        else:
                            color[nv] = not color[v]
                            nq.append(nv)
                q, nq = nq, []
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                if not bfs(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
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

        def bfs(i):
            q, nq = [i], []
            while q:
                for cur in q:
                    for nxt in graph[cur]:
                        if nxt in color:
                            if color[nxt] == color[cur]:
                                return False
                        else:
                            color[nxt] = not color[cur]
                            nq.append(nxt)
                q, nq = nq, []
            return True

        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                if not bfs(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
                        return False
            return True

        for i in range(n):
            if i not in color:
                color[i] = True
                if not dfs(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
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

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
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

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
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

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
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

        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
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
        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
                        return False
            return True

        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                if not dfs(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
                        return False
            return True

        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = True
                if not dfs(i):
                    return False
        return True


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i):
            for j in graph[i]:
                if j in color:
                    if color[j] == color[i]:
                        return False
                else:
                    color[j] = not color[i]
                    if not dfs(j):
                        return False
            return True

        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = True
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
