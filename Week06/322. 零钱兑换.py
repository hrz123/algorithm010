# 322. 零钱兑换.py
from collections import deque
from typing import List


# 暴力，递归，指数
# BFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        deq = deque([amount])
        coins.sort(reverse=True)
        res = -1
        while deq:
            size = len(deq)
            res += 1
            for _ in range(size):
                node = deq.popleft()
                if node < 0:
                    continue
                if node == 0:
                    return res

                deq.extend([node - coin for coin in coins])
        return -1


# 重复性，查找子问题，bfs
# 定义状态数组
# dp(i)是凑到i数额所需的最少硬币数
# dp(i) = min(dp(i-coin)) + 1
# 递推方程 f(n) = min{f(n-k) for k in [1,2,5]} + 1
# 初始状态 f(0) = 0, f(负数) = 最大值
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] > amount else dp[amount]


# 改进
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币

        amount_plus_one = amount + 1
        dp = [amount_plus_one] * amount_plus_one
        dp[0] = 0
        for i in range(1, amount_plus_one):
            dp[i] = min(
                dp[i - c] if c <= i else amount_plus_one for c in coins) + 1
        return -1 if dp[amount] > amount else dp[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]


# 以下为自我练习
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_value = float('inf')
        dp = [0] + [max_value] * amount
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else max_value for c in
                        coins) + 1
            if i == 1:
                print(dp[i])
        return -1 if dp[amount] == max_value else dp[amount]


def main():
    coins = [1, 2, 5]
    amount = 80
    sol = Solution()
    res = sol.coinChange(coins, amount)
    print(res)


if __name__ == '__main__':
    main()
