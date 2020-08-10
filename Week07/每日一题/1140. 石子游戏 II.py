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


# 以下为自我练习

# 定义一个dfs
# 参数为起始石子索引，当前M
# 返回玩家拿走前X 1<=x<=2M 后可以拿到的最大值
# dfs(start, m) = sub(start..n-1) - dfs(start+x, max(m, x)) for x in 1 ..  2m
# 终止条件
# 2*m >= n-i时，可以全拿走
# 可以记忆化
# sub(start..n-1)可以使用前缀和
# 最终返回dfs(0, 1)，索引为0，当前M为1的结果
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sub = [0] * (n + 1)
        for i in range(n):
            sub[i + 1] = sub[i] + piles[i]
        memo = {}

        def dfs(i, m):
            if (i, m) in memo:
                return memo[i, m]
            remain = sub[n] - sub[i]
            if m * 2 >= n - i:
                return remain
            memo[i, m] = 0
            for x in range(1, 2 * m + 1):
                memo[i, m] = max(memo[i, m], remain - dfs(i + x, max(x, m)))
            return memo[i, m]

        return dfs(0, 1)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pre = [0]
        p = 0
        for num in piles:
            p += num
            pre.append(p)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, m):
            remain = pre[n] - pre[i]
            if i + (m << 1) >= n:
                return remain
            res = 0
            for x in range(1, (m << 1) + 1):
                res = max(res, remain - dfs(i + x, max(m, x)))
            return res

        return dfs(0, 1)


def main():
    sol = Solution()

    piles = [2, 7, 9, 4, 4]
    res = sol.stoneGameII(piles)
    print(res)

    piles = [1, 2, 3, 4, 5, 100]
    res = sol.stoneGameII(piles)
    print(res)


if __name__ == '__main__':
    main()
