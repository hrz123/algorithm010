# 410. 分割数组的最大值.py
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = 0
        right = 0
        for num in nums:
            left = left if left > num else num
            right += num
        while left < right:
            mid = left + ((right - left) >> 1)
            # 初始值必须是一
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    total = num
                    count += 1
            if count > m:
                left = mid + 1
            else:
                right = mid

        return left


# dp解法
# 我们可以令 f[i][j] 表示将数组的前 i 个数分割为 j 段所能得到的最大连续子数组和的最小值
# 在进行状态转移时，我们可以考虑第 j 段的具体范围，
# 即我们可以枚举 k，其中前 k 个数被分割为 j−1 段，
# 而第 k+1 到第 i 个数为第 j 段。此时，这 j 段子数组中和的最大值，
# 就等于 f[k][j−1] 与 sub(k+1, i) 中的较大值，
# 其中 sub(i,j) 表示数组 nums 中下标落在区间 [i,j] 内的数的和。
# 由于我们要使得子数组中和的最大值最小，因此可以列出如下的状态转移方程
# f(i, j) = min ( max ( f(k, j-1), sub(k+1, i))) k 0..i-1
# 对于状态f(i, j)，由于我们能不能分出空的子数组，因此合法的状态 i >= j
# 对于不合法的状态，由于我们的目标是求出最小值，因此可以将这些状态全部初始化为一个很大的数
# 在上述转移方程中，一旦我们尝试从不合法的状态f(k, j-1)进行转移，那么max()将会是一个很大的数，
# 就不会对最外层的min()产生影响。
# 初始化
# 我们需要令f(0, 0)为0
# 在上述的转移方程中，j=1时，唯一的可能性就是前i个数被分成了1段
# 如果枚举k等于0，那么就代表着这种情况；
# 如k!=0, 对应的状态是不合法的，无法转移，所以我们需要f(0, 0) = 0
# 返回值
# f(n, m)
# 优化空间复杂度


# 定义子问题
# 前i个元素分成j组的最大连续数组和的最小值
# 定义状态数组
# f(i,j), i 0 .. n   j 0..m
# 递推方程
# f(i, j) = min(max(f(k, j-1) , sub(k, i-1)))， k 0..i-1
# 第i个的索引是i-1
# sub(k, i-1)表示k到i-1的连续数组和，包括两边
# 注意，不可以一组中什么都没有，所以j最大是i, j<=i
# 初始化
# 因为要求的是最小值，所以我们可以把不合法的地方都标为正无穷
# 因为f(1, 1) = min(max(f(0, 0), a[0])) 只有这一种情况
# 我们知道前一个元素分成1分 连续子数组的最大值的最小值是a[0]
# 所以我们不能初始化f(0, 0)为正无穷
# 我们要初始化f(0, 0)为0
# 返回值
# 返回f(n, m)
# 这里连续数组和可以用前缀和来快速求得
# 优化空间复杂度
# 无法优化
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        _max = float('inf')
        f = [[_max] * (m + 1) for _ in range(n + 1)]
        f[0][0] = 0
        sub = [0] * (n + 1)
        for i in range(n):
            sub[i + 1] = sub[i] + nums[i]
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                f[i][j] = min(max(f[k][j - 1], sub[i] - sub[k]) for k in
                              range(i))
        return f[n][m]


# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         _max = float('inf')
#         f = [[_max] * (m + 1) for _ in range(n + 1)]
#         # 前缀和
#         sub = [0] * (n + 1)
#         for i in range(n):
#             sub[i + 1] = sub[i] + nums[i]
#
#         f[0][0] = 0
#         for i in range(1, n + 1):
#             for j in range(1, min(i, m) + 1):
#                 for k in range(i):
#                     f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
#
#         return f[n][m]
#
#
# # 以下为自我练习
# # 二分法
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         lo, hi = 0, 0
#         for num in nums:
#             hi += num
#             lo = max(lo, num)
#         while lo < hi:
#             mid = lo + ((hi - lo) >> 1)
#             count = self.count_parts(nums, mid)
#             if count > m:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo
#
#     def count_parts(self, nums, _max):
#         count = 1
#         cur = 0
#         for num in nums:
#             cur += num
#             if cur > _max:
#                 count += 1
#                 cur = num
#         return count
#
#
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         l = r = 0
#         for n in nums:
#             l = max(l, n)
#             r += n
#         while l < r:
#             mid = l + ((r - l) >> 1)
#             count = self._count(nums, mid)
#             if count > m:
#                 l = mid + 1
#             else:
#                 r = mid
#         return l
#
#     def _count(self, nums, k):
#         count = 1
#         _sum = 0
#         for n in nums:
#             _sum += n
#             if _sum > k:
#                 count += 1
#                 _sum = n
#         return count


def main():
    sol = Solution()

    nums = [7, 2, 5, 10, 8]
    m = 2
    res = sol.splitArray(nums, m)
    print(res)

    nums = [1, 3, 5]
    m = 2
    res = sol.splitArray(nums, m)
    print(res)


if __name__ == '__main__':
    main()
