# 2.py
from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neigh = defaultdict(set)
        for x, y in roads:
            neigh[x].add(y)
            neigh[y].add(x)
        res = 0

        def maxRank(x, y):
            if y in neigh[x]:
                return len(neigh[x]) + len(neigh[y]) - 1
            return len(neigh[x]) + len(neigh[y])

        for x in range(n):
            for y in range(x + 1, n):
                res = max(res, maxRank(x, y))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
