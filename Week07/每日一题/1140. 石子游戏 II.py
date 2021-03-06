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
# dfs(start, n) = sub(start..m-1) - dfs(start+x, max(n, x)) for x in 1 ..  2m
# 终止条件
# 2*n >= m-i时，可以全拿走
# 可以记忆化
# sub(start..m-1)可以使用前缀和
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


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pre = [0]
        p = 0
        for pi in piles:
            p += pi
            pre.append(p)
        import functools
        @functools.lru_cache(None)
        def dfs(i, m):
            rest = pre[n] - pre[i]
            if i + (m << 1) >= n:
                return rest
            res = 0
            for x in range(1, (m << 1) + 1):
                res = max(res, rest - dfs(i + x, max(m, x)))
            return res

        return dfs(0, 1)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pre = [0]
        p = 0
        for pi in piles:
            p += pi
            pre.append(p)
        import functools
        @functools.lru_cache(None)
        def dfs(i, m):
            rest = pre[n] - pre[i]
            if i + (m << 1) >= n:
                return rest
            res = 0
            for x in range(1, (m << 1) + 1):
                res = max(res, rest - dfs(i + x, max(x, m)))
            return res

        return dfs(0, 1)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        pre = [0]
        p = 0
        for pile in piles:
            p += pile
            pre.append(p)
        import functools
        @functools.lru_cache(None)
        def dfs(i, m):
            rest = pre[n] - pre[i]
            if i + (m << 1) >= n:
                return rest
            res = max(
                rest - dfs(i + x, max(m, x)) for x in range(1, (m << 1) + 1))
            return res

        return dfs(0, 1)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        import functools
        @functools.lru_cache(None)
        def dfs(i, m):
            rest = pre[n] - pre[i]
            if i + m * 2 >= n:
                return rest
            res = 0
            for x in range(1, m * 2 + 1):
                res = max(res, rest - dfs(i + x, max(x, m)))
            return res

        pre = [0]
        p = 0
        for pile in piles:
            p += pile
            pre.append(p)
        n = len(piles)
        return dfs(0, 1)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        import functools
        @functools.lru_cache(None)
        def dfs(i, m):
            rest = pre[n] - pre[i]
            if i + m * 2 >= n:
                return rest
            res = 0
            for x in range(1, m * 2 + 1):
                res = max(res, rest - dfs(i + x, max(x, m)))
            return res

        pre = [0]
        p = 0
        for pile in piles:
            p += pile
            pre.append(p)
        n = len(piles)
        return dfs(0, 1)


def main():
    sol = Solution()

    piles = [2, 7, 9, 4, 4]
    res = sol.stoneGameII(piles)
    print(res)

    piles = [1, 2, 3, 4, 5, 100]
    res = sol.stoneGameII(piles)
    print(res)
    piles = [3111, 4303, 2722, 2183, 6351, 5227, 8964, 7167, 9286, 6626, 2347,
             1465, 5201, 7240, 5463, 8523, 8163, 9391, 8616, 5063, 7837, 7050,
             1246, 9579, 7744, 6932, 7704, 9841, 6163, 4829, 7324, 6006, 4689,
             8781, 621]
    res = sol.stoneGameII(piles)
    print(res)


if __name__ == '__main__':
    main()
