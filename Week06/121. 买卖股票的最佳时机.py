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


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre, cur = float('-inf'), 0
        for p in prices:
            cur = max(cur, p + pre)
            pre = max(pre, -p)
        return cur


# 定义子问题
# f(i, 01, 01)表示第i天，能不能买入(是否卖出），手里有没有股票的最大收入
#               不动          买入               卖出
# f(i, 0, 0) = f(i-1, 0, 0)  一直都为0
# f(i, 0, 1) = f(i-1, 0, 1)  f(i-1, 0, 0)-a[i]
# f(i, 1, 0) = f(i-1, 1, 0)                    f(i-1, 0, 1) + a[i]
# f(i, 1, 1) = 不能卖出还买入，没有意义
# 初始化和边界条件
# f01 = float('-inf')
# f10 = 0
# 返回值
# f10
# 优化复杂度
# 可以只用两个值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f01, f10 = float('-inf'), 0
        for p in prices:
            f01, f10 = max(f01, -p), max(f10, f01 + p)
        return f10


# 相当于公式是a[j]-a[i]，a[i]在j变化的时候是不变的，和观光问题是一样的
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plus, minus = 0, float('-inf')
        for p in prices:
            plus, minus = max(plus, minus + p), max(minus, -p)
        return plus


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
