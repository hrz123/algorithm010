# 5477. 排布二进制网格的最少交换次数.py
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zv = [-1] * n
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    zv[i] = j
        for idx, val in enumerate(sorted(zv)):
            if val > idx:
                return -1
        ans = 0
        for i in range(n):
            if zv[i] <= i:
                continue
            t = zv[i]
            j = i + 1
            while zv[j] > i:
                zv[j], t = t, zv[j]
                j += 1
            zv[i], zv[j] = zv[j], t
            ans += j - i
        return ans


def main():
    sol = Solution()
    grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
    res = sol.minSwaps(grid)
    print(res)


if __name__ == '__main__':
    main()
