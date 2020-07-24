# 1140. 石子游戏 II.py
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]

        def dfs(i, m):
            if i >= n:
                return 0
            if (i, m) in memo:
                return memo[(i, m)]
            if i + m * 2 >= n:
                return s[i]
            best = 0
            for x in range(1, 2 * m + 1):
                # 剩余石子减去对方最优策略
                best = max(best, s[i] - dfs(i + x, max(x, m)))
            memo[(i, m)] = best
            return memo[(i, m)]

        return dfs(0, 1)


def main():
    sol = Solution()

    piles = [2, 33, 9, 4, 4]
    res = sol.stoneGameII(piles)
    print(res)

    piles = [1, 2, 3, 4, 5, 100]
    res = sol.stoneGameII(piles)
    print(res)


if __name__ == '__main__':
    main()
