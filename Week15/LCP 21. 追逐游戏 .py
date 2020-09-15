# LCP 21. 追逐游戏 .py
import collections
from typing import List


class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int,
                  startB: int) -> int:
        n = max(max(i) for i in edges)
        grid = [set() for i in range(n + 1)]
        for i, j in edges:
            grid[i].add(j)
            grid[j].add(i)

        def bfs(start):
            res = [-1] * (n + 1)
            que = collections.deque([start])
            res[start] = 0
            while que:
                p = que.popleft()
                for i in grid[p]:
                    if res[i] == -1:
                        res[i] = res[p] + 1
                        que.append(i)
            return res

        la, lb = bfs(startA), bfs(startB)
        if la[startB] == 1: return 1
        res = 1
        for i, j in zip(la, lb):
            if i - j > 1:
                res = max(res, i)
        que = []
        for i in range(1, n + 1):
            if len(grid[i]) == 1:
                que.append(i)
        while que:
            x = que.pop()
            for i in grid[x]:
                grid[i].remove(x)
                if len(grid[i]) == 1:
                    que.append(i)
            grid[x].pop()
        que = []
        for i in range(1, n + 1):
            if len(grid[i]) > 1:
                que.append(i)

        def dfs(start, leave, pre, target):
            if leave == 0: return True
            for i in grid[start]:
                if i == pre: continue
                if i == target: return False
                if not dfs(i, leave - 1, start, target):
                    return False
            return True

        for i in que:
            if la[i] - lb[i] < 2: continue
            if dfs(i, 3, -1, i):
                return -1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
