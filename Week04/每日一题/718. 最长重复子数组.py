# 718. 最长重复子数组.py
from typing import List


# 状态定义：dp(n,m)，A到m，B到n位置最长重复子数组，且必须包含m，n位置对应的元素
# 递推方程
# if A(n) == B(m)   ,dp(n, m) = dp(n-1, m-1) + 1
# else   , dp(n, m) = 0
# 起始条件 dp(0, m) = 0, dp(n, 0) = 0
# n 从0到A的length， m 从0到B的length
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        lenA = len(A)
        lenB = len(B)

        # 空间复杂度做到最低可以使用
        if lenA < lenB:
            lenA, lenB = lenB, lenA
            A, B = B, A

        dp = [0] * (lenB + 1)
        res = 0

        for i in range(lenA):
            dp_ = [0] * (lenB + 1)
            for j in range(lenB):
                if A[i] == B[j]:
                    tmp = dp[j] + 1
                    res = max(res, tmp)
                    dp_[j + 1] = tmp
                else:
                    dp_[j + 1] = 0
            dp = dp_

        return res


# 时间复杂度：O(n*m)，因为m+1 * m+1的矩阵都要遍历一次。mn为AB的长度
# 空间复杂度，可以使用AB长度的最小值。

# 子问题
# dp(start, j)定义为到i和j且包含i和j的最长重复子数组的长度
# 定义状态数组
# dp(start, j) = dp(start-1, j-1)+1 if a[start] == b[j]
#          = 0              else
#
# 初始化 dp(0, 0)
# 发现在增加一维更方便
# 那就增加一维
# dp(0, j) = 0 j 0..len(b)
# dp(start, 0) = 0 start 0..len(a)
# dp(start, j) = dp(start-1, dpj-1) + 1 if a[start-1] == b[start-1] else 0
# 发现状态数组可以优化
# 用一个数组就可以
# 递推方程
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if m < n:
            m, n = n, m
            A, B = B, A
        dp = [0] * (n + 1)
        max_len = 0
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]:
                    dp[j + 1] = dp[j] + 1
                    max_len = max(max_len, dp[j + 1])
                else:
                    dp[j + 1] = 0
        return max_len


# 定义子问题
# A到第i个数，(索引为i-1), B到第j个数，公共的长度最长的子数组的长度，
# 且该数组的最后一位就是A[start-1]和B[j-1]，是多少
# 定义状态为f(start, j)
# 递推方程
# f(start, j) = if A[start-1] == B[j-1] f(start-1, j-1) + 1
#           else 0
# start = 0..len(A) j = 0..len(B)
# 初始化
# f(0, j) = 0 j = 0..len(B)
# f(start, 0) = 0 start = 0..len(A)
# 返回值
# 返回f(start, j)中的最大值
# 优化空间复杂度，
# 我们可以使用一个一位数组，从后往前递推
# 这样最少使用len(A)和len(B)中的较小者
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        a_len, b_len = len(A), len(B)
        if a_len < b_len:
            a_len, b_len = b_len, a_len
            A, B = B, A
        dp = [0] * (b_len + 1)
        res = 0
        for i in range(a_len):
            for j in range(b_len, 0, -1):
                if A[i] == B[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
        return res


# 定义子问题
# f(i, j)为s[:i], t[:j]的最长子数组长度，且一定包含s[i]t[j]
# 递推方程
# f(i, j) = f(i-1, j-1) + 1 if s[i] == t[j]
#         = 0 else
# 初始化
# f(0, j) = 0
# f(j, 0) = 0
# 返回值这些中最大的
# 优化复杂度
# 可以只用一维数组，从后往前原地更新
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if m < n:
            m, n = n, m
            A, B = B, A
        dp = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n - 1, -1, -1):
                dp[j + 1] = dp[j] + 1 if A[i] == B[j] else 0
                res = max(res, dp[j + 1])
        return res


# 定义子问题
# f(i, j)为s[:i] t[:j]的最长子数组长度，且该子数组一定包含最后一个索引的元素
# f(i, j) =  if s[i] == t[j] f(i, j) = f(i-1, j-1) + 1
# f(i, j) =   else 0
# 初始化和 边界条件
# f(i, 0) = 0
# f(0, j) = 0
# 边界条件是i，j大于等于1
# 返回值，f(i,j)中的最大值
# 优化复杂度
# i， j至于i-1,j-1有关，我们从后往前可以原地更新数组
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if m < n:
            m, n = n, m
            A, B = B, A
        dp = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n - 1, -1, -1):
                dp[j + 1] = dp[j] + 1 if A[i] == B[j] else 0
                res = max(res, dp[j + 1])
        return res


# 定义子问题，以s[i] t[j]的公共最长子数组长度，一定以s[i] t[j]结尾
# f(i, j) = f(i-1, j-1) + 1 if s[i] == t[j]
# f(i, j) = 0 else
# 初始化和边界条件
# f(0, j) = 0
# f(i, 0) = 0
# 返回值
# f(i, j)中最大的
# 优化复杂度
# 我们需要两个数组滚动，数组长度为两个数组中较短的那一个
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if m < n:
            m, n = n, m
            A, B = B, A
        res = 0
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    ndp[j + 1] = dp[j] + 1
                    res = max(res, ndp[j + 1])
                else:
                    ndp[j + 1] = 0
            dp, ndp = ndp, dp
        return res


# 定义子问题
# f(i, j)为s[:i]与t[:j]的最长子数组的长度，必须包含结尾元素
# if s[i] = t[j]
# f(i, j) = f(i-1, j-1) + 1
# else:
# f(i, j) = 0
# 初始化和边界条件
# f(0, j) = 0
# f(i, 0) = 0
# 返回值，f(i,j)中的最大值
# 优化复杂度
# 我们可以用一个数组，从后往前原地更新，取最小厂区
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        if m < n:
            m, n = n, m
            A, B = B, A
        dp = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]:
                    dp[j + 1] = dp[j] + 1
                    res = max(res, dp[j + 1])
                else:
                    dp[j + 1] = 0
        return res


def main():
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    sol = Solution()
    res = sol.findLength(A, B)
    print(res)


if __name__ == '__main__':
    main()
