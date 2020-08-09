# 121. 买卖股票的最佳时机.py
from typing import List


# 只能完成一笔交易
# 子问题
# 定义状态数组: f(start)为第i+1天卖出的最大值, max(f(start))
# 递推方程
# f(start) = max(f(start-1) + a[start] - a[start-1], 0)
# f(0) = 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = 0
        res = 0
        for i in range(1, len(prices)):
            x += prices[i] - prices[i - 1]
            x = max(x, 0)
            res = max(res, x)
        return res


# 以下为自我练习
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_value = prices[0]
        res = 0
        for p in prices:
            if p < min_value:
                min_value = p
            res = max(res, p - min_value)
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        res = 0
        for i in range(1, len(prices)):
            profit = max(0, prices[i] - prices[i - 1] + profit)
            res = max(res, profit)
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x, y = float('-inf'), 0
        for p in prices:
            x, y = max(x, -p), max(y, x + p)
        return y


def main():
    sol = Solution()

    nums = [7, 1, 5, 3, 6, 4]
    res = sol.maxProfit(nums)
    print(res)

    nums = [7, 6, 5, 4, 3]
    res = sol.maxProfit(nums)
    print(res)


if __name__ == '__main__':
    main()
