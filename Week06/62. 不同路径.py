# 62. 不同路径.py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m

        dp = [1] * m

        for _ in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[j] = dp[j] + dp[j + 1]
        return dp[0]


# 以下为自我练习
# 子问题从i，j到m-1, n-1的不同路径是多少
# 定义状态数组
# f(start, j)
# 递推方程
# f(start,j) = f(start+1, j) + f(start, j+1)
# 初始化
# f(m-1, n-1) = 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]
        return dp[0]


# 子问题
# 定义状态数组
# 递推方程
# f(start, j) = f(start+1, j) + f(start, j+1)
# 初始化
# f(m-1, n-1) = 1
# 优化空间复杂度
# 只使用一维数组即可，m,n中取最小值
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]
        return dp[0]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]
        return dp[0]


# f(i, j) = f(i-1, j) +f(i, j-1)
# 初始化
# f(0, 0) = 1
# f(0, j) = 1
# f(i, 0) = 1
# 使用哨兵
# 0， 1， 000
# 返回值 f(m, n)
# 优化，使用一维数组，原地更新
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        dp = [0, 1] + [0] * (n - 1)
        for _ in range(m):
            for j in range(n):
                dp[j + 1] += dp[j]
        return dp[n]


def main():
    m = 7
    n = 3
    sol = Solution()
    res = sol.uniquePaths(m, n)
    print(res)


if __name__ == '__main__':
    main()
