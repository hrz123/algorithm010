# 53. 最大子序和.py
from typing import List


# 重复性
# 状态数组定义：dp(start)，表示到i位置且包括i的最大和数组
# 递推方程：dp(start) = max(0, dp(start-1)) + a(start)
# dp(0) = a[0]
# 返回max(dp)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = 0
        res = nums[0]

        for num in nums:
            dp = max(dp, 0) + num
            res = max(res, dp)

        return res


# 以下为自我练习
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        res = dp
        for i in range(1, len(nums)):
            dp = max(dp, 0) + nums[i]
            res = max(res, dp)
        return res


# 子问题
# 定义到i位置，且必须包含i位置的连续数组最大和为dp(start)
# 最终返回max(dp(start)), start 0..n-1
# 定义状态数组
# dp(start)
# 递推方程
# dp(start) = max(dp(start-1), 0) + arr[start]
# 初始化dp(0) = arr[0]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = nums[0]
        global_max = local_max
        for i in range(1, len(nums)):
            local_max = max(0, local_max) + nums[i]
            global_max = max(global_max, local_max)
        return global_max


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _sum, res = 0, float('-inf')
        for num in nums:
            _sum = max(_sum + num, num)
            res = max(res, _sum)
        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, res = 0, float('-inf')
        for num in nums:
            pre = max(num, pre + num)
            res = max(pre, res)
        return res


# 时间复杂度：O(n)
# 空间复杂度：O(1)

# 线段树
# 我们定义一个操作get(a, l, r)表示查询a序列[l, r]区间内的最大子段和，
# 那么最终我们要求的答案就是get(arr, 0, n-1)。如何分治实现这个操作呢？
# 对于一个区间l, r，我们取m = (l + r)/2， 对区间[l,m] 和 [m+1, r]分治求解。
# 当递归逐层深入直到区间长度缩小为1的时候，递归「开始回升」。
# 这个时候我们考虑如何通过[l, m]区间的信息和[m+1, r]区间的信息合并成区间[l, r]的信息。
# 最关键的两个问题是：
# 我们要维护区间的哪些信息呢？
# 我们如何合并这些信息？
# 对于一个区间[l, r]，我们可以维护四个量：
# lSum表示[l, r]内以l为左端点的最大子段和
# rSum表示[l, r]内以r为右端点的最大字段和
# mSum表示[l, r]内的最大子段和
# iSum表示[l, r]的区间和
# 以下简称[l, m]为[l, r]的「左子区间」，[m+1, r]为[l, r]的右子区间。
# 我们考虑如何维护这些量呢（如何通过左右子区间的信息合并得到[l,r]的信息）？
# 对于长度为1的区间[start,start]，四个量的值都和ai相等。对于长度大于1的区间：
# 首先最好维护的是iSum，区间[l, r]的iSum就等于「左子区间」的iSum加上「右子区间」的iSum。
# 对于[l, r]的lSum，存在两种可能，它要么等于「左子区间」的lSum，
# 要么等于「左子区间」的iSum加上「右子区间」的lSum，两者取大。
# 对于[l, r]的rSum，同理，它要么等于「右子区间」的rSum，
# 要么等于「右子区间」的iSum加上「左子区间」的rSum，两者取大
# 当计算好上面的三个量之后，就很好计算[l, r]的mSum了。
# 我们可以考虑[l, r]的mSum对应的区间是否跨越m--它可能不跨越m，
# 也就是说[l, r]的mSum可能是「左子区间」的mSum和「右子区间」
# 的mSum中的一个；
# 它可能跨越m，可能是「左子区间」的rSum和「右子区间」的lSum求和。三者取大。
# 时间复杂度，相当于遍历一个二叉树的所有结点，结点最多为2*n个，所以时间为O(n)
# 空间复杂度：递归：O(logn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        return self.get(nums, l, r)[2]

    def get(self, nums, l, r):
        if l == r:
            return [nums[l]] * 4

        mid = l + ((r - l) >> 1)
        lSum1, rSum1, mSum1, iSum1 = self.get(nums, l, mid)
        lSum2, rSum2, mSum2, iSum2 = self.get(nums, mid + 1, r)
        iSum = iSum1 + iSum2
        lSum = max(lSum1, iSum1 + lSum2)
        rSum = max(rSum2, iSum2 + rSum1)
        mSum = max(mSum1, mSum2, rSum1 + lSum2)
        return lSum, rSum, mSum, iSum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        return self.get(nums, l, r)[2]

    def get(self, nums, l, r):
        if l == r:
            return [nums[l]] * 4
        mid = l + ((r - l) >> 1)
        lSum1, rSum1, mSum1, iSum1 = self.get(nums, l, mid)
        lSum2, rSum2, mSum2, iSum2 = self.get(nums, mid + 1, r)
        iSum = iSum1 + iSum2
        lSum = max(lSum1, iSum1 + lSum2)
        rSum = max(rSum2, rSum1 + iSum2)
        mSum = max(mSum1, mSum2, rSum1 + lSum2)
        return [lSum, rSum, mSum, iSum]


# 存储一颗线段树
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        memo = {}
        res = self.build(nums, l, r, memo)[2]
        print(memo)
        return res

    def build(self, nums, l, r, memo):
        if l == r:
            memo[l, r] = [nums[l]] * 4
            return [nums[l]] * 4

        mid = l + ((r - l) >> 1)
        lSum1, rSum1, mSum1, iSum1 = self.build(nums, l, mid, memo)
        lSum2, rSum2, mSum2, iSum2 = self.build(nums, mid + 1, r, memo)
        iSum = iSum1 + iSum2
        lSum = max(lSum1, iSum1 + lSum2)
        rSum = max(rSum2, iSum2 + rSum1)
        mSum = max(mSum1, mSum2, rSum1 + lSum2)
        memo[l, r] = [lSum, rSum, mSum, iSum]
        return lSum, rSum, mSum, iSum


# f(i) s[:i]的最大子序和，且一定包括i
# f(i) = max(f(i-1), 0) + a[i]
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, cur = float('-inf'), float('-inf')
        for n in nums:
            pre = max(pre + n, n)
            cur = max(cur, pre)
        return cur


# 「方法二」相较于「方法一」来说，时间复杂度相同，但是因为使用了递归，并且维护了四个信息的结构体，
# 运行的时间略长，空间复杂度也不如方法一优秀，而且难以理解。
# 那么这种方法存在的意义是什么呢？
#
# 对于这道题而言，确实是如此的。但是仔细观察「方法二」，它不仅可以解决区间 [0,n−1]，
# 还可以用于解决任意的子区间 [l,r] 的问题。
# 如果我们把 [0,n−1] 分治下去出现的所有子区间的信息都用堆式存储的方式记忆化下来，
# 即建成一颗真正的树之后，我们就可以在 O(logn) 的时间内求到任意区间内的答案，
# 我们甚至可以修改序列中的值，做一些简单的维护，
# 之后仍然可以在 O(logn) 的时间内求到任意区间内的答案，
# 对于大规模查询的情况下，这种方法的优势便体现了出来。
# 这棵树就是上文提及的一种神奇的数据结构——线段树。

# f(i)定义为s[:i]的最大子序和，且一定包含i这个位置
# f(i) = max(f(i-1) + s[i] , s[i])
# 初始化和边界条件
# f(0) = 0
# f(1) = max(f(0)+s[i], s[i])
# 返回值，这些值中的最大值
# 优化空间复杂度，我们只需要一个数值，存f(i-1)即可
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f0 = 0
        res = float('-inf')
        for n in nums:
            f0 = max(f0 + n, n)
            res = max(res, f0)
        return res


# f(i) = max(f(i-1) + n, n)
# 初始化
# f(0) = 0
# f(1)
# 返回值
# res = max(fi)
# 初始化成一个最小值
# 优化复杂度
# 只需要前一个值，并且我们记录一个最大值
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, res = 0, float('-inf')
        for n in nums:
            pre = max(pre + n, n)
            res = max(res, pre)
        return res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, res = 0, float('-inf')
        for num in nums:
            pre = max(pre + num, num)
            res = max(res, pre)
        return res


# 最大子序和
# f(i)表示以下标i字符结尾的最长子序和的大小
# f(i) = max(f(i-1)+a, a)
# 初始化
# pre可以用0初始化
# res 要用一个最小值来初始化
# 返回 max(f(i))
# 优化复杂度
# 只需要一个变量
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, res = 0, float('-inf')
        for num in nums:
            pre = max(pre + num, num)
            res = max(res, pre)
        return res


def main():
    sol = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = sol.maxSubArray(nums)
    print(res)

    nums = [-1]
    res = sol.maxSubArray(nums)
    print(res)


if __name__ == '__main__':
    main()
