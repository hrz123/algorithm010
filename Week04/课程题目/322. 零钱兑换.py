# 322. 零钱兑换.py
from functools import lru_cache
from typing import List


# 状态定义: 凑成总金额n最少需要多少个硬币
# 递推方程：
# dp(n) = min(dp(n-coins[i])) + 1
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
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币

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
