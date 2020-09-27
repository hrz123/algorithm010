# 4.py


# f(i, j, 0) = max(f(i + 1, j, 1) + a[i], f(i, j - 1, 1) + a[j])
# f(i, j, 1) = f(i + 1, j, 0) f(i, j - 1, 1)

# 初始化
# f(i, i, 0) = a[i]
# f(i, i, 1) = 0
class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = values[i]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                left = dp[i + 1][j][1] + values[i]
                right = dp[i][j - 1][1] + values[j]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[0][n - 1][0] > dp[0][n - 1][1]


def main():
    pass


if __name__ == '__main__':
    main()
