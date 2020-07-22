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
# 返回值
# 优化空间复杂度
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        f00 = f10 = 0
        f01 = -prices[0]

        for i in range(1, len(prices)):
            price = prices[i]
            f00, f01, f10 = max(f00, f10), max(f01, f00 - price), f01 + price
        return max(f00, f10)


# 定义子问题
# 到第i天，可以不可以买入股票（当天是否卖出）j，0表示可以，1表示不可以，k手里的股票数
# 定义状态数组
# f(i, 0, 0), f(i, 0, 1) f(i, 1, 1)
# 递推方程

# f(i, 0, 0) = 不动 max f(i-1, 0, 0) f(i-1, 1, 0)
# f(i, 0, 1) = max 不动 f(i-1, 0, 1) 买入 f(i-1, 0, 0) -a[i]
# f(i, 1, 0) = 卖出 f(i-1, 0, 1) + a[i]

# 初始化
# f(0, 0, 0 = f(0, 1, 0) = 0, f(0, 0, 1) = -a[0]

# 返回值
# 返回 f(n-1, 0, 0) f(n-1, 1, 0)中较大的

# 优化空间复杂度
# 用三个数就可以了
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        f00, f01, f10 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            price = prices[i]
            f00, f01, f10 = max(f00, f10), max(f01, f00 - price), f01 + price

        return max(f00, f10)


def main():
    nums = [1, 2, 3, 0, 2]
    sol = Solution()
    res = sol.maxProfit(nums)
    print(res)


if __name__ == '__main__':
    main()
