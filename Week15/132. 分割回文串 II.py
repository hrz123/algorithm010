# 132. 分割回文串 II.py


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]
        for i in range(1, n):
            if s[:i + 1] == s[:i + 1][::-1]:
                dp[i] = 0
                continue
            dp[i] = min(dp[j] + 1 for j in range(i)
                        if s[j + 1:i + 1] == s[j + 1:i + 1][::-1])
        return dp[n - 1]


def main():
    sol = Solution()
    s = "aab"
    res = sol.minCut(s)
    print(res)


if __name__ == '__main__':
    main()
