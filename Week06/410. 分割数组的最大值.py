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
# 我们可以令 f[start][j] 表示将数组的前 start 个数分割为 j 段所能得到的最大连续子数组和的最小值
# 在进行状态转移时，我们可以考虑第 j 段的具体范围，
# 即我们可以枚举 k，其中前 k 个数被分割为 j−1 段，
# 而第 k+1 到第 start 个数为第 j 段。此时，这 j 段子数组中和的最大值，
# 就等于 f[k][j−1] 与 sub(k+1, start) 中的较大值，
# 其中 sub(start,j) 表示数组 arr 中下标落在区间 [start,j] 内的数的和。
# 由于我们要使得子数组中和的最大值最小，因此可以列出如下的状态转移方程
# f(start, j) = min ( max ( f(k, j-1), sub(k+1, start))) k 0..start-1
# 对于状态f(start, j)，由于我们能不能分出空的子数组，因此合法的状态 start >= j
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
# f(start,j), start 0 .. n   j 0..m
# 递推方程
# f(start, j) = min(max(f(k, j-1) , sub(k, start-1)))， k 0..start-1
# 第i个的索引是i-1
# sub(k, start-1)表示k到i-1的连续数组和，包括两边
# 注意，不可以一组中什么都没有，所以j最大是i, j<=start
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
#     def splitArray(self, arr: List[int], m: int) -> int:
#         n = len(arr)
#         _max = float('inf')
#         f = [[_max] * (m + 1) for _ in range(n + 1)]
#         # 前缀和
#         sub = [0] * (n + 1)
#         for start in range(n):
#             sub[start + 1] = sub[start] + arr[start]
#
#         f[0][0] = 0
#         for start in range(1, n + 1):
#             for j in range(1, min(start, m) + 1):
#                 for k in range(start):
#                     f[start][j] = min(f[start][j], max(f[k][j - 1], sub[start] - sub[k]))
#
#         return f[n][m]
#
#
# # 以下为自我练习
# # 二分法
# class Solution:
#     def splitArray(self, arr: List[int], m: int) -> int:
#         lo, hi = 0, 0
#         for num in arr:
#             hi += num
#             lo = max(lo, num)
#         while lo < hi:
#             mid = lo + ((hi - lo) >> 1)
#             log2_minus_1 = self.count_parts(arr, mid)
#             if log2_minus_1 > m:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo
#
#     def count_parts(self, arr, _max):
#         log2_minus_1 = 1
#         cur = 0
#         for num in arr:
#             cur += num
#             if cur > _max:
#                 log2_minus_1 += 1
#                 cur = num
#         return log2_minus_1
#
#
# class Solution:
#     def splitArray(self, arr: List[int], m: int) -> int:
#         l = row = 0
#         for n in arr:
#             l = max(l, n)
#             row += n
#         while l < row:
#             mid = l + ((row - l) >> 1)
#             log2_minus_1 = self._count(arr, mid)
#             if log2_minus_1 > m:
#                 l = mid + 1
#             else:
#                 row = mid
#         return l
#
#     def _count(self, arr, k):
#         log2_minus_1 = 1
#         _sum = 0
#         for n in arr:
#             _sum += n
#             if _sum > k:
#                 log2_minus_1 += 1
#                 _sum = n
#         return log2_minus_1
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


# 定义子问题
# 前i个数分成j个数组的各自和的最大值
# 定义状态数组
# f(start, j) start 1..n 1..min(start,m)
# 递推方程
# f(start, j) = min(max(f(k, j-1), sub(k+1, start))  k j-1.. start-1)
# 初始化
# 我们可以使用哨兵初始化
# 我们唯一知道的就是f(1, 1)第一个数只有一个数组时就是a[1]
# 那么f(0, 0)只能是0
# 其余位置，因为我们会取最小值，我们可以都设置为一个最大值
# 返回值
# f(n, m)
# 优化空间复杂度
# 不好优化
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        sub = [0] * (n + 1)
        for i in range(n):
            sub[i + 1] = sub[i] + nums[i]
        f = [[sub[n]] * (m + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                f[i][j] = min(max(f[k][j - 1], sub[i] - sub[k])
                              for k in range(i))
        return f[n][m]


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = 0, 0
        for num in nums:
            lo = max(lo, num)
            hi += num
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self._count(nums, mid) > m:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _count(self, nums, val):
        count = 1
        total = 0
        for n in nums:
            total += n
            if total > val:
                count += 1
                total = n
        return count


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = 0, 0
        for n in nums:
            lo = max(lo, n)
            hi += n
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self._count(nums, mid) > m:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _count(self, nums, mid):
        c = 1
        p = 0
        for n in nums:
            p += n
            if p > mid:
                c += 1
                p = n
        return c


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = 0, 0
        for n in nums:
            lo = max(lo, n)
            hi += n
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self._count(nums, mid) > m:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _count(self, nums, mid):
        c = 1
        p = 0
        for n in nums:
            p += n
            if p > mid:
                c += 1
                p = n
        return c


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
