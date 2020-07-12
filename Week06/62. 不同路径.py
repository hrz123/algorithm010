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


def main():
    m = 7
    n = 3
    sol = Solution()
    res = sol.uniquePaths(m, n)
    print(res)


if __name__ == '__main__':
    main()
