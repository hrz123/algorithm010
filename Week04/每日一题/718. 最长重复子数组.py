# 718. 最长重复子数组.py
from typing import List


# 状态定义：dp(m,n)，A到m，B到n位置最长重复子数组，且必须包含m，n位置对应的元素
# 递推方程
# if A(m) == B(n)   ,dp(m, n) = dp(m-1, n-1) + 1
# else   , dp(m, n) = 0
# 起始条件 dp(0, n) = 0, dp(m, 0) = 0
# m 从0到A的length， n 从0到B的length
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


# 时间复杂度：O(m*n)，因为m+1 * n+1的矩阵都要遍历一次。mn为AB的长度
# 空间复杂度，可以使用AB长度的最小值。

# 子问题
# dp(i, j)定义为到i和j且包含i和j的最长重复子数组的长度
# 定义状态数组
# dp(i, j) = dp(i-1, j-1)+1 if a[i] == b[j]
#          = 0              else
#
# 初始化 dp(0, 0)
# 发现在增加一维更方便
# 那就增加一维
# dp(0, j) = 0 j 0..len(b)
# dp(i, 0) = 0 i 0..len(a)
# dp(i, j) = dp(i-1, dpj-1) + 1 if a[i-1] == b[i-1] else 0
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


def main():
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    sol = Solution()
    res = sol.findLength(A, B)
    print(res)


if __name__ == '__main__':
    main()
