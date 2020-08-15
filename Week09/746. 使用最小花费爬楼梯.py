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


# f(i) = 为到达第i层的花费
# f(i) = min(f(i-1), f(i-2)) + a[i]
# 初始化
# f(0) = 0
# f(1) = a[0]
# 我们递推一下
# f(2) = min(f(1), f(0)) + a[1] = min(a[0], 0) + a[1] = a[1]
# 没问题
# 我们有没有可能再用一层哨兵
# f(1) = min(f(0), f(-1)) + a[0]，我们完全可以再用一层哨兵，令f(-1) = 0
# 这样所有的递推都符合我们的条件
# 我们的代码可以更简洁
# 返回值
# 我们返回 n-1层和n-2层中的较小值
# 优化复杂度
# 我们只需要两个数存储结果
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0, f1 = 0, 0
        for c in cost:
            f0, f1 = f1, min(f0, f1) + c
        return min(f0, f1)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0, f1 = 0, 0
        for c in cost:
            f0, f1 = f1, min(f0, f1) + c
        return min(f0, f1)


# 到达f(i)的最小花费
# f(i) = min(f(i-1), f(i-2)) + p
# 初始化
# f(0) = 0
# f(1) = a[0]
# f(2) = a[1]
# 再加一层哨兵f(-1)=0也可以
# 返回值f(n)和f(N-1)中的较小值
# 优化复杂度
# 只需要两个值
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0, f1 = 0, 0
        for c in cost:
            f0, f1 = f1, min(f0, f1) + c
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
