# 1557. 可以到达所有点的最少点数目.py
from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[
        int]:
        neigh = defaultdict(list)
        for i, j in edges:
            neigh[j].append(i)
        res = []
        for i in range(n):
            if i not in neigh:
                res.append(i)
        return res


def main():
    sol = Solution()
    n = 5
    edges = [[1, 3], [2, 0], [2, 3], [1, 0], [4, 1], [0, 3]]
    res = sol.findSmallestSetOfVertices(n, edges)
    print(res)


if __name__ == '__main__':
    main()
