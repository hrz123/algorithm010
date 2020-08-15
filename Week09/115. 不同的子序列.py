# 115. 不同的子序列.py


# 定义子问题
# s[:start]中子序列出现t[:j}的个数
# 定义状态数组
# f(start, j)
# if s[start-1] == t[j-1]
# f(start, j) = f(start-1, j-1) + f(start-1, j)  start >= j
# else
# f(start, j) = f(start-1, j)
# 初始化
# f(0, 0) = 1
# f(start, j) = 0 if start < j
# f(start, 0) = 1
# 返回值
# 返回f(m, n)
# 优化空间复杂度
# 从后往前推，只需要原地改变数组
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(min(i, n - 1), -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[n]


# 定义子问题
# f(i, j) s[:i]中出现t[:j]的次数
# f(i, j) s[i] == t[j] === f(i-1, j-1) + f(i-1, j)
#         else    f(i-1, j)
# 初始化和边界条件
# f(0, 0) = 1  f（0,k) = 0
# i >= j
# 返回值f(m, n)
# 优化空间复杂度
# 用一个长度为len(t)+1的数组，从len(t)到0可以原地更新
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(min(i, n - 1), -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[n]


# 以下为自我练习
# 定义子问题
# f(i, j)  s[:i]中T[:j]出现的个数
# f(i, j) = f(i-1, j-1) (if s[i] == T[j]) + f(i-1, j)
#           f(i-1, j)
# 初始化和边界条件
# f(0, 0) = 1
# i >= j 否则不可能出现
# 返回值
# f(m, n)
# 优化空间复杂度
# 只需要j这个维度就可以
# 从后往前递推，可以原地更新
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(min(i, n - 1), -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[n]


# 定义子问题
# f(i, j)表示s[:i]中t[:j]出现的个数
# f(i, j) if s[i] == t[j] = f(i-1, j-1) + f(i-1, j)
# f(i, j) = f(i-1, j)
# 初始化和边界条件
# f(1, 1) = f(0, 0) + f(0, 1) = 1,所以f(0, 0) = 1
# f(i, j) i>=j
# 返回值f(m, n)
# 优化复杂度
# 从后往前可以原地更新
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(min(i, n - 1), -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[n]


# 定义子问题
# f(i, j) 为s[:i]的子序列中t[:j]出现的个数
# f(i, j) = if s[i] == t[j] = f(i-1, j-1) + f(i-1, j)
#           else f(i-1, j)
# 初始化和边界条件
# f(i, j) i一定大于等于j
# f(0, 0) = 1
# f(0, j) = 0, j != 0
# 递推一下
# f(1, 1) = f(0, 0) + f(0, 1)
# f(3, 1) = f(2, 0) + f(2, 1)
# f(i, 0) = 1
# 没问题
# 返回值f(m, n)
# 优化复杂度
# 我们只需要一维数组，从后往前递推，大小为t的长度
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[n]


def main():
    sol = Solution()

    S = "rabbbit"
    T = "rabbit"
    res = sol.numDistinct(S, T)
    print(res)

    S = "babgbag"
    T = "bag"
    res = sol.numDistinct(S, T)
    print(res)


if __name__ == '__main__':
    main()
