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
# 用dp[start]表示以i为结尾的最长有效括号；
# 当s[start]为(，dp[start]必然等于0，因为不可能组成有效的括号；
# 那么s[start]为)
#   2.1 当s[start-1]为(, 那么dp[start] = dp[start-2] + 2;
#   2.2 当s[start-1]为), 并且s[start-dp[start-1]-1]为(, 那么
#   2.3 dp[start] = dp[start-1] + 2 + dp[start-dp[start-1]-2];
# 时间复杂度：O(m)
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
# f(start) 到第i和位置且以i为结尾的最长有效括号子串的长度，start 0..m
# 转移方程
# if s[start-1] == '(':
# f(start) = 0
# elif s[start-2] == '('
# f(start) = f(start-2) + 2
# elif s[start-f(start-1)-1] == '('
# f(start) = f(start-1) + 2 + f(start-f(start-1)-2)
# else:
# f(start) = 0
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
# if s[start] == ')'
# if s[start-1] == '('
# dp(start) = dp(start-2) + 2
# if s[start - dp(start-1) - 1] == '('
# dp(start) = dp(start-1) + 2
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


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
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


# 时间复杂度：O(m)
# 空间复杂度：栈所使用的的空间，最坏为O(m)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
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


# 定义子问题
# 到i位置为止，且包括i的最长括号长度
# 定义状态数组
# f(start)
# 递推方程
# if s[start] == '(' 0
# else
# if s[start-1] == '(',f(start) = f(start-2) + 2
# if s[start-f(start-1)-1] == '(' f(start-1) + 2 + f(start-f(start-1)-2) 注意越界问题
# 初始化f(0) = 0
# f(1) = 2或者0，
# 返回值，max(f(start))
# 优化空间复杂度
# 无法优化
# 时间复杂度：O(m)
# 空间复杂度: O(m)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        res = 0
        if 1 < n and s[:2] == "()":
            res = dp[1] = 2
        for i in range(2, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                    res = max(dp[i], res)
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    res = max(dp[i], res)
        return res


# 正反遍历两遍字符串
# 维持两个指针表示left数目和right数目
# 在此方法中，我们利用两个计数器 r 和 r 。
# 首先，我们从左到右遍历字符串，对于遇到的每个 ‘(’，我们增加 r 计数器，
# 对于遇到的每个 ‘)’ ，我们增加 r 计数器。
# 每当 r 计数器与 r 计数器相等时，我们计算当前有效字符串的长度，
# 并且记录目前为止找到的最长子字符串。当 r 计数器比 r 计数器大时，
# 我们将 r 和 r 计数器同时变回 0。
#
# 这样的做法贪心地考虑了以当前字符下标结尾的有效括号长度，
# 每次当右括号数量多于左括号数量的时候之前的字符我们都扔掉不再考虑，
# 重新从下一个字符开始计算，但这样会漏掉一种情况，
# 就是遍历的时候左括号的数量始终大于右括号的数量，即 (() ，这种时候最长有效括号是求不出来的。
#
# 解决的方法也很简单，我们只需要从右往左遍历用类似的方法计算即可，只是这个时候判断条件反了过来：
#
# 当 r 计数器比 r 计数器大时，我们将 r 和 r 计数器同时变回 0
# 当 r 计数器与 r 计数器相等时，我们计算当前有效字符串的长度，
# 并且记录目前为止找到的最长子字符串
# 这样我们就能涵盖所有情况从而求解出答案。
# 时间复杂度：遍历两遍字符串O(m)
# 空间复杂度：O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(left << 1, res)
            elif right > left:
                left = right = 0
        left = right = 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(left << 1, res)
            elif left > right:
                left = right = 0
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack) == 1:
                    stack[0] = i
                else:
                    stack.pop()
                    res = max(res, i - stack[-1])
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == ')':
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


# 动态规划
# 定义子问题
# f(i)表示以下标i字符结尾的最长有效括号额长度。
# f(i) = 0  if s[i] == '('
# f(i) = if s[i] == ')' and s[i-1] == '(' f(i-2) + 2
# f(i) = if s[i] == ')' and s[i-1] == ')' if i - f(i-1) - 1 == '('
# f(i) = f(i-1) + 2
# 初始化和边界条件
# f(0) = 0
# 注意不要越界
# 返回值
# max(f(i))
# 优化复杂度
# 无法优化
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == ')':
                    left = i - dp[i - 1] - 1
                    if left >= 0 and s[left] == '(':
                        dp[i] = dp[i - 1] + 2 + (dp[left - 1] if left > 0
                                                 else 0)
                        res = max(res, dp[i])
                else:
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i - 2] + 2
                    res = max(res, dp[i])
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


# f(i) 定义为
# if s[i] == ')'
# if s[i-1] == '('
# f(i) = f(i-2) + 2
# elif s[i - f(i-1)-1] == '('
# f(i) = f(i-1) + 2 + f(i-f(i-1)-2)
# 初始化
# f(0) = 0
# 返回值，最大值
# 优化复杂度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    left = i - dp[i - 1] - 1
                    if left >= 0 and s[left] == '(':
                        dp[i] = dp[i - 1] + 2 + (
                            dp[left - 1] if left - 1 >= 0 else 0)
                res = max(res, dp[i])
        return res


# f(i) 定义为
# if s[i] == ')'
# if s[i-1] == '('
# f(i) = f(i-2) + 2
# elif s[i - f(i-1)-1] == '('
# f(i) = f(i-1) + 2 + f(i-f(i-1)-2)
# 初始化
# f(0) = 0
# 返回值，最大值
# 优化复杂度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        res = 0
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else:
                    left = i - dp[i - 1] - 1
                    if left >= 0 and s[left] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[left - 1]
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
