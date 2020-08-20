# 面试题 16.19. 水域大小.py
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1),
                (-1, 1))
        m, n = len(land), len(land[0])
        res = []

        def dfs(i, j):
            res = 1
            land[i][j] = -1
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and land[_i][_j] == 0:
                    res += dfs(_i, _j)
            return res

        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    res.append(dfs(i, j))
        res.sort()
        return res


def main():
    sol = Solution()
    land = [
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]
    res = sol.pondSizes(land)
    print(res)


if __name__ == '__main__':
    main()
