# 213. 打家劫舍 II.py
from typing import List


# 子问题
# 定义状态数组
# f(start, j) 表示第i家， start:0..n-1, j, 0..1, 0表示不偷第一家，1表示偷
# 递推方程:
# f(start, j) = max(f(start-1, j), f(start-2, j) + arr[start])
# f(n-1, 1) = max(f(n-2, 1), f(n-3,j))
# 初始条件
# f(0, 0) = 0
# f(0, 1) = arr[0]
# f(1, 0) = arr[1]
# f(1, 1) = arr[0]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [[0] * 2 for _ in range(2)]
        dp[0][1] = nums[0]
        dp[1][0] = nums[1]
        dp[1][1] = nums[0]

        for i in range(2, len(nums) - 1):
            num = nums[i]
            dp[0][0], dp[1][0] = dp[1][0], max(dp[1][0], dp[0][0] + num)
            dp[0][1], dp[1][1] = dp[1][1], max(dp[1][1], dp[0][1] + num)
        dp[0][0], dp[1][0] = dp[1][0], max(dp[1][0], dp[0][0] + nums[-1])
        dp[0][1], dp[1][1] = dp[1][1], max(dp[0][1], dp[1][1])

        return max(dp[1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(helper(nums[:-1]), helper(nums[1:])) \
            if len(nums) != 1 else nums[0]


# 以下为自我练习
# 定义子问题
# 到第i天且使用了偷了第0天的，必须使用第i天
# 注意
# 那么就返回f(n-1,0) f(n-2, 0) f(n-2, 1) f(n-3,1) 的最大值 0表示没使用第0天
# 定义状态数组
# f(start, 1)使用了第1天的 f(start,0)没使用第1天
# 递推方程
# f(start, 0) = max(f(start-2, 0), f(start-3, 0)) + a[start]
# f(start, 1) = max(f(start-2, 1), f(start-3, 1)) + a[start]
# 初始化
# f(0, 0) = float('-inf')
# f(1, 0) = a[1]
# f(2, 0) = a[2]
# f(0, 1) = a[0]
# f(1, 1) = float('-inf')
# f(2, 1) = a[0] + a[2]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        min_value = float('-inf')
        f00, f10, f20, f01, f11, f21 = (
            min_value, nums[1], nums[2], nums[0], min_value, nums[0] + nums[2]
        )

        for i in range(3, n):
            f00, f10, f20, f01, f11, f21 = (
                f10,
                f20,
                max(f10, f00) + nums[i],
                f11,
                f21,
                max(f11, f01) + nums[i]
            )
        return max(f20, f10, f11, f01)


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return nums[0] if len(nums) == 1 else max(helper(nums[:-1]), helper(
            nums[1:]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            pre, cur = 0, 0
            for num in nums:
                pre, cur = cur, max(cur, pre + num)
            return cur

        return nums[0] if len(nums) == 1 else max(helper(nums[:-1]), helper(
            nums[1:]))


def main():
    sol = Solution()

    nums = [2]
    res = sol.rob(nums)
    print(res)

    nums = [2, 3, 2]
    res = sol.rob(nums)
    print(res)

    nums = [1, 2, 3, 1]
    res = sol.rob(nums)
    print(res)

    nums = [2, 7, 9, 3, 1]
    res = sol.rob(nums)
    print(res)


if __name__ == '__main__':
    main()
