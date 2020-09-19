# 808.分汤.py


class Solution(object):
    def soupServings(self, N):
        Q, R = divmod(N, 25)
        N = Q + (R > 0)
        if N >= 500:
            return 1

        memo = {}

        def dp(x, y):
            if (x, y) not in memo:
                if x <= 0 or y <= 0:
                    ans = 0.5 if x <= 0 and y <= 0 else 1.0 if x <= 0 else 0.0
                else:
                    ans = 0.25 * (dp(x - 4, y) + dp(x - 3, y - 1) + dp(x - 2,
                                                                       y - 2) + dp(
                        x - 1, y - 3))
                memo[x, y] = ans
            return memo[x, y]

        return dp(N, N)


def main():
    sol = Solution()
    res = sol.soupServings(12500)
    print(res)


if __name__ == '__main__':
    main()
