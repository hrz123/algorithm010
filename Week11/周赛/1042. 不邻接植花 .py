# 1042. 不邻接植花 .py
from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths):
        color = [1] * N
        graph = [[] for _ in range(N)]
        for path in paths:
            if path[0] > path[1]:
                graph[path[0] - 1].append(path[1] - 1)
            else:
                graph[path[1] - 1].append(path[0] - 1)
        for i in range(1, N):
            flower = [1, 2, 3, 4]
            for node in graph[i]:
                if color[node] in flower:
                    flower.remove(color[node])
            color[i] = flower[0]
        return color


# 以下为自我练习
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        color = [1] * N
        neigh = defaultdict(list)
        for i, j in paths:
            if i > j:
                neigh[i - 1].append(j - 1)
            else:
                neigh[j - 1].append(i - 1)
        for i in range(N):
            flower = [1, 2, 3, 4]
            for j in neigh[i]:
                if color[j] in flower:
                    flower.remove(color[j])
            color[i] = flower[0]
        return color


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        color = [1] * N
        neigh = defaultdict(list)
        for i, j in paths:
            if i > j:
                neigh[i - 1].append(j - 1)
            else:
                neigh[j - 1].append(i - 1)
        for i in range(N):
            flower = [1, 2, 3, 4]
            for node in neigh[i]:
                if color[node] in flower:
                    flower.remove(color[node])
            color[i] = flower[0]
        return color


def main():
    sol = Solution()
    n = 3
    nums = [[1, 2], [2, 3], [3, 1]]
    res = sol.gardenNoAdj(n, nums)
    print(res)

    n = 6
    nums = [[6, 4], [6, 1], [3, 1], [4, 5], [2, 1], [5, 6], [5, 2]]
    res = sol.gardenNoAdj(n, nums)
    print(res)


if __name__ == '__main__':
    main()
