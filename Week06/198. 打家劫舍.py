# 198. 打家劫舍.py
from typing import List


# 子问题：偷第几家房子f(start)有重复性
# 定义状态数组： 偷到第i个房子并且偷第i个房子
# 递推方程：
# f(start) = max(f(start-2), f(start-3)) + a[start]
# f(0) = 0
# f(1) = a[0]
# f(2) = a[1]
# 最大状态为max(f(n), f(n-1))
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i - 1]

        return max(dp[n - 1:])


# 改进
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * 4
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(2, n):
            dp[3] = max(dp[:2]) + nums[i]
            dp[:3] = dp[1:]
        return max(dp[1:3])


# 时间复杂度： O(n)
# 空间复杂度： O(n)


# a[start]: 0..start 能偷到 max value: a[n-1]
# a[start][0, 1]: 0:i偷， 1：i不偷
# a[start][0] = max(a[start-1][0], a[start-1][1])
# a[start][1] = a[start-1][0] + arr
# a[0][0] = 0
# a[0][1] = arr[0]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0] * 2 for _ in range(2)]

        dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            dp[1][0] = max(dp[0])
            dp[1][1] = dp[0][0] + nums[i]

            dp[0][:] = dp[1]

        return max(dp[0])


# a[start]: 0..start 能偷到 max value: a[n]
# a[start]: 0..i天，且nums[start]或者nums[start-1]必偷
# a[start] = max(a[start-2] + arr[start], a[start-1])
# a[0] = arr[0]
# a[1] = max(arr[:1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * 3
        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, n):
            dp[2] = max(dp[0] + nums[i], dp[1])
            dp[:2] = dp[1:]

        return dp[1]


# 改进
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        prev_max = nums[0]
        cur_max = max(nums[:2])

        for i in range(2, n):
            prev_max, cur_max = cur_max, max(prev_max + nums[i], cur_max)

        return cur_max


# 改进
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = cur_max = 0
        for num in nums:
            prev_max, cur_max = cur_max, max(prev_max + num, cur_max)
        return cur_max


# 以下为自我练习
# 定义子问题
# 到第i间房屋的最高金额，且第i间房屋一定偷
# 返回 f(n-1) f(n-2)中的最大值
# 定义状态数组
# f(start)
# 递推方程
# f(start) = max(f(start-2), f(start-3)) + a[start]
# 初始化
# f(0) = a[0]
# f(1) = a[1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp0 = nums[0]
        dp1 = nums[1]
        dp2 = dp0 + nums[2]
        for i in range(3, n):
            dp2, dp1, dp0 = max(dp0, dp1) + nums[i], dp2, dp1
        return max(dp2, dp1)


# 定义子问题为一定包含i这个点的最大利润
# f(start) = max(f(start-2), f(start-3)) + a[start]
# 最终返回max(f(n-1), f(n-2))
# 初始化
# f(0) = a[0]
# f(1) = a[1]
# f(2) = a[0] + a[2]
# 可以递推了
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)

        f0, f1, f2 = nums[0], nums[1], nums[0] + nums[2]

        for i in range(3, n):
            f0, f1, f2 = f1, f2, max(f1, f0) + nums[i]
        return max(f1, f2)


# 另一种递推
# 状态定义：

# 设动态规划列表 dp ，dp[start] 代表前 start 个房子在满足条件下的能偷窃到的最高金额。
# 转移方程：

# 设： 有 n 个房子，前 n 间能偷窃到的最高金额是 dp[n] ，前 n−1 间能偷窃到的最高金额是 dp[n−1] ，
# 此时向这些房子后加一间房，此房间价值为 num ；
# 加一间房间后： 由于不能抢相邻的房子，意味着抢第 n+1 间就不能抢第 n 间；
# 那么前 n+1 间房能偷取到的最高金额 dp[n+1] 一定是以下两种情况的 较大值 ：
# 不抢第 n+1 个房间，因此等于前 n 个房子的最高金额，即 dp[n+1] = dp[n]；
# 抢第 n+1 个房间，此时不能抢第 n 个房间；因此等于前 n−1 个房子的最高金额加上当前房间价值，
# 即 dp[n+1] = dp[n-1] + num；
# 细心的我们发现： 难道在前 n 间的最高金额 dp[n] 情况下，第 n 间一定被偷了吗？
# 假设没有被偷，那 n+1 间的最大值应该也可能是 dp[n+1]=dp[n]+num 吧？
# 其实这种假设的情况可以被省略，这是因为：
# 假设第 n 间没有被偷，那么此时 dp[n]=dp[n−1] ，此时 dp[n+1]=dp[n]+num=dp[n−1]+num ，
# 即可以将 两种情况合并为一种情况 考虑；
# 假设第 n 间被偷，那么此时 dp[n+1]=dp[n]+num 不可取 ，因为偷了第 n 间就不能偷第 n+1 间。
# 最终的转移方程： dp[n+1]=max(dp[n],dp[n−1]+num)
# 初始状态：

# 前 0 间房子的最大偷窃价值为 0 ，即 dp[0]=0 。
# 返回值：

# 返回 dp 列表最后一个元素值，即所有房间的最大偷窃价值。
# 简化空间复杂度：

# 我们发现 dp[n] 只与 dp[n−1] 和 dp[n−2] 有关系，
# 因此我们可以设两个变量 cur和 pre 交替记录，将空间复杂度降到 O(1) 。
class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur


class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur


# f(start) = f(start-1), f(start-2) + a[start]
class Solution:
    def rob(self, nums: List[int]) -> int:
        f0, f1 = 0, 0
        for n in nums:
            f0, f1 = f1, max(f1, f0 + n)
        return f1


# f(i) = f(i-1), a+f(i-2)
class Solution:
    def rob(self, nums: List[int]) -> int:
        f0, f1 = 0, 0
        for num in nums:
            f0, f1 = f1, max(f1, f0 + num)
        return f1


def main():
    sol = Solution()

    nums = [1, 2, 3, 1]
    res = sol.rob(nums)
    print(res)

    nums = [2, 7, 9, 3, 1]
    res = sol.rob(nums)
    print(res)


if __name__ == '__main__':
    main()
