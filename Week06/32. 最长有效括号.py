# 32. 最长有效括号.py


# 子问题 到i位置，且以i为结尾的最长有效括号子串的长度
# 我们不停的更新这个长度，同时记录这个字符串，最终这个返回最长的字符串即可
# 定义状态数组
# f(i) 到第i和位置且以i为结尾的最长有效括号子串的长度，i 0..n
# 转移方程
# if s[i-1] == '(':
# f(i) = 0
# elif s[i-2] == '('
# f(i) = f(i-2) + 2
# elif s[i-f(i-1)-1] == '('
# f(i) = f(i-1) + 2 + f(i-f(i-1)-2)
# else:
# f(i) = 0
# 初始化
# f(0) = 0，什么都没有的时候为0
# f(1) = 0, 只有一个括号一定为0
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        n = len(s)

        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            if s[i - 1] == "(":
                continue
            elif s[i - 2] == "(":
                dp[i] = dp[i - 2] + 2
                res = max(res, dp[i])
            elif i - 2 - dp[i - 1] >= 0 and s[i - 2 - dp[i - 1]] == "(":
                dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
                res = max(res, dp[i])
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        n = len(s)

        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            if s[i - 1] == ")":
                if s[i - 2] == "(":
                    dp[i] = dp[i - 2] + 2
                elif i - 2 - dp[i - 1] >= 0 and s[i - 2 - dp[i - 1]] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
                res = max(res, dp[i])

        return res


def main():
    sol = Solution()
    s = "(()"
    res = sol.longestValidParentheses(s)
    print(res)

    s = ")(()))"
    res = sol.longestValidParentheses(s)
    print(res)

    s = "()(())"
    res = sol.longestValidParentheses(s)
    print(res)

    s = "(()))())("
    res = sol.longestValidParentheses(s)
    print(res)


if __name__ == '__main__':
    main()
