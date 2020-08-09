# 322. 零钱兑换.py
from functools import lru_cache
from typing import List


# 状态定义: 凑成总金额n最少需要多少个硬币
# 递推方程：
# dp(n) = min(dp(n-coins[start])) + 1
# 起始条件
# dp[0] = 0
# dp[负数] = float("inf")
# 递归的方式
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amount: int):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            return min([dfs(amount - coin) for coin in coins]) + 1

        res = dfs(amount)
        return -1 if res == float('inf') else res


# 正向递推
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向上
        # dp[start] 表示金额为i需要最少的硬币
        # dp[start] = min(dp[start], dp[start - coins[j]]) j所有硬币

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(
                dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
        return -1 if dp[-1] == float("inf") else dp[-1]


# 以下为自我练习
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_value = float('inf')
        dp = [0] + [max_value] * amount

        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i >= c else max_value for c in coins) + 1

        return -1 if dp[amount] == max_value else dp[amount]


# 定义子问题
# f(start)到i这个总数需要的最小银币数
# 定义状态数组
# f(start)
# 递推方程
# f(start) = min(f(start-c)) for c in coins + 1
# 初始化
# f(0) = 0
# f(一个负数)可以认为是正无穷，这样在有硬币组合能组成总金额的时候就可以取最小值忽略掉
# 返回值
# f(amount)
# 优化空间复杂度
# 没必要，空间复杂度和coins中的最大值有关
# 时间复杂度：O(n * m) n是amount的值，m是coins的个数
# 空间复杂度：O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        _max = float('inf')
        dp = [0] + [_max] * amount
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] + 1 if i >= c else _max for c in coins)
        return -1 if dp[amount] == _max else dp[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        _max = float('inf')
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] + 1 if i >= c else _max for c in coins)
        return -1 if dp[amount] == _max else dp[amount]


# f(i)
# 递推方程
# f(i) = min(f(i-c)) + 1 for c in coins
# 初始化，f(0) = 0
# 其他的值我们为了不影响其他求min的操作，我们设为一个极大值
# 返回值f(amount)如果不为极大值
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]


def main():
    sol = Solution()

    coins = [1, 2, 5]
    amount = 11
    res = sol.coinChange(coins, amount)
    print(res)

    coins = [2]
    amount = 3
    res = sol.coinChange(coins, amount)
    print(res)


if __name__ == '__main__':
    main()
