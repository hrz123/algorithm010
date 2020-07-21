# 518. 零钱兑换 II.py
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(1, amount + 1):
                dp[i] += dp[i - c] if i >= c else 0
        return dp[amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(1, amount + 1):
                if i >= c:
                    dp[i] += dp[i - c]
        return dp[amount]


def main():
    sol = Solution()

    amount = 5
    coins = [1, 2, 5]
    res = sol.change(amount, coins)
    print(res)

    amount = 3
    coins = [2]
    res = sol.change(amount, coins)
    print(res)

    amount = 10
    coins = [10]
    res = sol.change(amount, coins)
    print(res)


if __name__ == '__main__':
    main()
