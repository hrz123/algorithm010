# 312. 戳气球.py
from typing import List


# 子问题很明显
# 戳破之后的硬币最大数量
# 定义状态方程
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        max_coin = 0

        def dfs(level, length, before_coins):
            nonlocal max_coin
            if length == level:
                if before_coins > max_coin:
                    max_coin = before_coins
                    return

            for i in range(length):
                if nums[i] == -1:
                    continue
                tmp = nums[i]
                nums[i] = -1

                before = i - 1
                while before >= 0 and nums[before] == -1:
                    before -= 1
                if before == -1:
                    before_num = 1
                else:
                    before_num = nums[before]

                after = i + 1
                while after < length and nums[after] == -1:
                    after += 1
                if after == length:
                    after_num = 1
                else:
                    after_num = nums[after]

                dfs(level + 1, length,
                    before_coins + tmp * after_num * before_num)

                nums[i] = tmp

        dfs(0, len(nums), 0)
        return max_coin


# 暴力回溯
# 阶乘时间复杂度

# 子问题
# 思路：
# 在使用分治法时，我们应该考虑的核心问题是如何用子问题的解来表示原问题的解，
# 也就是子问题该如何划分才能通过子问题来求解原问题。
# 这道题的子问题是，在不戳破两边的情况下，戳破中间气球得到硬币的最大值
# 在这两个子问题解决后，气球序列还剩下k和两边的气球没有被戳破
# 那么我们用两个子问题的解与戳破k与两个边界的最大值即可求出原问题的解
# 定义状态数组
# f(i, j) = max(f(i, k) + f(k, j) + nums[i]*nums[k]*nums[j]) k = i + 1..j - 1
# f(i, i+1) = 0
# 递推方程
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def dfs(i, j):
            if dp[i][j] or j == i + 1:
                return dp[i][j]
            res = 0
            for k in range(i + 1, j):
                res = max(res,
                          dfs(i, k) + dfs(k, j) + nums[i] * nums[k] * nums[j])
            dp[i][j] = res
            return dp[i][j]

        return dfs(0, n - 1)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:  # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i + 1, j):  # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] +
                            calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   nums[i] * nums[k] * nums[j] + dp[i][k] +
                                   dp[k][j])
        return dp[0][n - 1]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[
                        i] * nums[j] * nums[k])
        return dp[0][n - 1]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] +
                                   dp[k][j] +
                                   nums[i] * nums[j] * nums[k])
        return dp[0][n - 1]


def main():
    sol = Solution()

    nums = [3, 1, 5, 8]
    res = sol.maxCoins(nums)
    print(res)


if __name__ == '__main__':
    main()
