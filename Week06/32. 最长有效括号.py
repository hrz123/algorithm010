# 32. 最长有效括号.py


# 1.
# 常规
# 对于这种括号匹配问题，一般都是使用栈。
# 我们先找到所有可以匹配的索引号，然后找出最长连续数列！
# 例如：s = )(()()), 我们可以用栈找到，
# 位置2和位置3匹配，
# 位置4和位置5匹配，
# 位置1和位置6匹配，
# 这个数组为：2，3，4，5，1，6 这是通过栈找到的，按递增排序。
# 1，2，3，4，5，6
# 找出该数组的最长连续数列的长度就是最长有效括号长度
# 所以时间复杂度来自排序：O(nlogn)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            elif s[i] == "(":
                stack.append(i)
        res.sort()
        # print(res)
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans


# stack只记录最后一个合法字符串位置
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


# 2.
# 用dp[i]表示以i为结尾的最长有效括号；
# 当s[i]为(，dp[i]必然等于0，因为不可能组成有效的括号；
# 那么s[i]为)
#   2.1 当s[i-1]为(, 那么dp[i] = dp[i-2] + 2;
#   2.2 当s[i-1]为), 并且s[i-dp[i-1]-1]为(, 那么
#   2.3 dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2];
# 时间复杂度：O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 \
                        and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res


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


# 以下为自我练习
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i + 1] = dp[i - 1] + 2
                    res = max(res, dp[i + 1])
                else:
                    if i - dp[i] - 1 >= 0 and s[i - dp[i] - 1] == '(':
                        dp[i + 1] = dp[i] + dp[i - dp[i] - 1] + 2
                        res = max(res, dp[i + 1])
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                max_len = max(max_len, i - stack[-1])
        return max_len


# 定义子问题
# 定义状态数组
# if s[i] == ')'
# if s[i-1] == '('
# dp(i) = dp(i-2) + 2
# if s[i - dp(i-1) - 1] == '('
# dp(i) = dp(i-1) + 2
# 初始化：dp(0) = 0
# dp(1) = 0
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        max_len = 0
        for i in range(2, n + 1):
            if s[i - 1] == ')':
                if s[i - 2] == '(':
                    dp[i] = dp[i - 2] + 2
                    max_len = max(max_len, dp[i])
                elif i - dp[i - 1] - 2 >= 0 and s[i - dp[i - 1] - 2] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    max_len = max(max_len, dp[i])
        return max_len


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
