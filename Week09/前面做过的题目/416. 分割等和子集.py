# 416. 分割等和子集.py
from typing import List


# 定义子问题
# 到了i这个索引，j这个数字能不能取到
# 定义状态数组
# f(start, j)
# 递推方程
# f(start, j) = f(start-1, j) or f(start - 1, j - a[start])
# 初始化
# 初始化全部为False，将f(0, a[0]) 和 f(0, 0)初始化为True，注意要判断越界
# start 0 .. n-1 j 0 .. target
# 返回值，一旦f(k, target)为True，返回True，否则返回False
# 优化空间复杂度
# 我们只需要两个数组来回表示i-1和i的情况即可
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        dp = [True] + [False] * target
        if nums[0] <= target:
            dp[nums[0]] = True
        ndp = [False] * (target + 1)
        for i in range(1, len(nums)):
            if dp[target]:
                return True
            for j in range(target + 1):
                ndp[j] = dp[j] or dp[j - nums[i]]
            dp, ndp = ndp, dp
        return dp[target]


# 以下为自我练习

# 定义子问题
# 画一个len行，target+1列的表格。这里len是误拼的个数，target是背包的容量。
# len行表示一个一个物品考虑，target+1多出来的那1列，表示背包容量从0开始，很多时候
# 我们需要考虑这个容量为0的数值。
# dp(start, j)表示从数组的[0..start]这个子区间中挑选一些数，每个数只能用一次，使得这些数的和恰好等于j
# 递推方程
# 状态转移方程：很多时候，状态转移方程思考的角度是“分类讨论”，
# 对于“0-1 背包问题”而言就是“当前考虑到的数字选与不选”。
# 不选择nums[start]，如果在[0， start-1]这个子区间内已经有一部分元素，使得它们的和为j
# 那么dp[start][j] 为True
# 选择nums[start]，如果在[0， start-1]这个子区间内能找得到一部分元素，使得它们的和为j-nums[start]
# dp[start][j] = dp[start-1][j] or dp[start-1][j-nums[start]]
# 边界条件
# j - nums[start] >=0
# 返回值
# dp[len-1][target]
# 优化空间复杂度
# 只需要前一索引，从后往前更新可以原地
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        n = len(nums)
        dp = [True] + [False] * target
        for i in range(n):
            for j in range(target, 0, -1):
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]


# 定义子问题
# f(start,j)为nums[:start]中能有跳出一些数，使得这些数的和为j
# 递推方程
# f(start, j) = 这个不拿 f(start-1, j) or 这个拿f(start-1, j-nums[start])
# 初始化和边界条件
# f(0, 0) = True f(0, k) = False
# j >= nums[start]
# 返回值
# f(n, target)
# 优化空间复杂度
# 只需要target+1那么长的数组，从target往前递推的时候可以原地
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        dp = [True] + [False] * target
        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[target]


# f(i, j)s[:i}是否能凑出j这个数
# f(i, j) = f(i-1, j) or f(i-1, j-nums[i])
# 初始化和边界条件
# f(0, 0) = True
# j >= nums[i]
# 返回值f(n, target)
# 优化空间复杂度
# 只需要一维数组
# j从后往前递推可以原地更新
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        dp = [True] + [False] * target
        for n in nums:
            for j in range(target, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]
        return dp[target]


# 定义子问题
# f(i, j)s[:i]中j这个值能不能取到
# f(i, j) = f(i-1, j) or f(i-1, j-p)
# 初始化和边界条件
# f(0, 0) = True, 其他的值都为False
# f(1, )是满足的
# j要大于等于p
# 只包含正整数，所以所有的负数都拿不到
# 返回值f(n, target)
# 优化复杂度，空间上只需要i-1和i天，其中只依赖j和j-p，都小于等于j，可以从后往前原地递推
# 我们只看target能不能拿到，所以大于target的值我们都可以忽略
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        dp = [True] + [False] * target
        for n in nums:
            for j in range(target, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]
            if dp[target]:
                return True
        return False


# f(i, j) s[:i]能不能凑出j
# f(i, j) = f(i-1, j) or f(i - 1, j-p) j>= p
# 初始化和边界条件
# f(0, 0) = True
# f(0, j) = False
# 因为只包含正整数，所以有最大值
# 另外因为我们只关心是否能到target
# 所以数组长度可以只到target
# 返回值f(i, target)
# 优化复杂度
# 我么从后往前可以原地更新
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        dp = [True] + [False] * target
        for n in nums:
            for j in range(target, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]
            if dp[target]:
                return True
        return False


# 定义子问题
# f(i, j) s[:i]能否凑出j
# f(i, j) = f(i-1, j) or f(i-1, j-p)
# 初始化和边界条件
# f(0, 0) = True
# f(0, j) = False j != 0
# 注意j>=p
# 返回值
# f(n , j)
# 优化复杂度
# 只与f(i-1)有关，我们从大到小可以原地更新
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        dp = [True] + [False] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
            if dp[target]:
                return True
        return False


def main():
    sol = Solution()

    nums = [1, 5, 5, 11]
    res = sol.canPartition(nums)
    print(res)

    nums = [1, 1]
    res = sol.canPartition(nums)
    print(res)

    nums = [2, 2, 3, 5]
    res = sol.canPartition(nums)
    print(res)


if __name__ == '__main__':
    main()
