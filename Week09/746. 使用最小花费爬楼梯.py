# 746. 使用最小花费爬楼梯.py
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0, f1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            f0, f1 = f1, min(f0, f1) + cost[i]
        return min(f0, f1)


# 以下为自我练习
# 定义子问题
# f(i)为到达i层的最小花费
# 到达i层的最小花费应该等于到达i-1层和到达i-2层的花费的较小者，再加上本层
# f(i) = min(f(i-1), f(i-2)) + a[i]
# 初始化和边界条件
# f(1) = a[0]
# f(2) = a[1]
# 如果我们要求到达第3层的花费，应该返回min(f(1), f(2))
# 返回值
# 我们应该求出n-1层和n-2层的值，然后求二者的较小者
# 优化空间复杂度
# 只需要两个变量
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f0, f1 = cost[0], cost[1]
        for i in range(2, n):
            f0, f1 = (f1, min(f0, f1) + cost[i])
        return min(f0, f1)


def main():
    sol = Solution()

    nums = [10, 15, 20]
    res = sol.minCostClimbingStairs(nums)
    print(res)

    nums = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = sol.minCostClimbingStairs(nums)
    print(res)


if __name__ == '__main__':
    main()
