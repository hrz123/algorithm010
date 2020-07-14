# 309. 最佳买卖股票时机含冷冻期.py
from typing import List


# 子问题
# 定义状态数组
# f(i, j, k) i 0..n-1表示第几天, j0..1表示可不可以买，0表示可以，k 0..1表示当前手里的股票
# max{f(n-1, 0, 0), f(n-1, 1, 0)
# 递推方程
# f(i, 0, 0) = max{f(i-1, 0, 0), f(i-1, 1, 0)}
# f(i, 0, 1) = max{f(i-1, 0, 1), f(i-1, 0, 0) - a[i])}
# f(i, 1, 0) = f(i-1, 0, 1) + a[i]
# 起始状态
# f(0, 0, 0) = 0
# f(0, 0, 1) = -a[0]
# f(0, 1, 0) = 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        d00 = d10 = 0
        d01 = -prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            d00, d01, d10 = max(d00, d10), max(d01, d00 - price), d01 + price
        return max(d00, d10)


def main():
    nums = [1, 2, 3, 0, 2]
    sol = Solution()
    res = sol.maxProfit(nums)
    print(res)


if __name__ == '__main__':
    main()
