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
# f(i, j)
# 递推方程
# f(i,j) = f(i+1, j) + f(i, j+1)
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


def main():
    m = 7
    n = 3
    sol = Solution()
    res = sol.uniquePaths(m, n)
    print(res)


if __name__ == '__main__':
    main()
