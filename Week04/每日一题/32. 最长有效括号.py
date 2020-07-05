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


def main():
    pass


if __name__ == '__main__':
    main()
