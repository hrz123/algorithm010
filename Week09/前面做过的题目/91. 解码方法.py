# 91. 解码方法.py
from functools import lru_cache


# 定义子问题
# s[:start]位置解码方法有多少种
# 定义状态数组
## dp(start) 0..n
# 递推方程
# f(start) = f(start-1) + f(start-2) if 0 < s[start-2:start] <= 26 and s[start-1] !=0
# f(start) = f(start-1)          if s[start-1] !=0
# f(start) = f(start-2)          if 0 < s[start-2:start] <= 26
# f(start) = 0               else
# f(0) = 1
# f(1) = 0  if s[0] == 0
# f(1) = 1  else
# 可以压缩到只用两个数
class Solution:
    def numDecodings(self, s: str) -> int:
        dp0 = 1
        dp1 = 0 if s[0] == '0' else 1

        for i in range(len(s) - 1):
            if 10 <= int(s[i:i + 2]) <= 26 and s[i + 1] != '0':
                dp0, dp1 = dp1, dp1 + dp0
            elif s[i + 1] != '0':
                dp0 = dp1
            elif 10 <= int(s[i:i + 2]) <= 26:
                dp0, dp1 = dp1, dp0
            else:
                dp0, dp1 = dp1, 0
        return dp1


# 以下为自我练习

# 子问题
# 子问题为s[:start]的解码方法，start 0..n n = len(s)
# 定义状态数组
# f(start)
# 递推方程
# f(start) = f(start-1) + f(start-2)  if 10<=int(s[start-2:start])<=26 and s[start-1] != 0
#      = f(start-1)           elif s[start-1] != 0
#      = f(start-2)           elif 10<=int(s[start-2:start])<=26
#      = 0                else
# 初始化
# f(0) = 1
# f(1) = 1 if s[0] != 0 else 0
# 最少需要两个数
class Solution:
    def numDecodings(self, s: str) -> int:
        dp0 = 1
        dp1 = 0 if s[0] == '0' else 1
        n = len(s)
        for i in range(2, n + 1):
            # 剪枝
            if not dp1:
                return 0
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':
                dp1, dp0 = dp1 + dp0, dp1
            elif s[i - 1] != '0':
                dp0 = dp1
            elif 10 <= int(s[i - 2:i]) <= 26:
                dp1, dp0 = dp0, dp1
            else:
                dp1, dp0 = 0, dp1
        return dp1


class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1

        cnt = 0

        if s[0] != '0':
            cnt += self.numDecodings(s[1:])
        if 10 <= int(s[0:2]) <= 26:
            cnt += self.numDecodings(s[2:])
        return cnt


class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        cnt = 0
        if s[0] != '0':
            cnt += self.numDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26:
            cnt += self.numDecodings(s[2:])
        return cnt


# dp
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        f0, f1 = 1, 1
        for i in range(1, n):
            f0, f1 = f1, (0 if s[i] == '0' else f1) \
                     + (f0 if 10 <= int(s[i - 1:i + 1]) <= 26 else 0)
        return f1


# dp(i)
# dp(i) = dp(i-1) if s[i] != 0
#         dp(i-2) if 10<=int(s[i-2:i])<=26
#         0
# 这个0是会传递下去的
# 比如30，到0个这个位置，最多0个解码方法，下一个位置无论是什么，
# 必然不会有这个条件 if 10<=int(s[i-2:i])<=26
# 而上一个条件的结果为0
# 所以将一直都是0
# 初始化和边界条件
# 空字符串的解码方式有一种
# dp[0] = 1， dp[1] = 1如果s[0]！='0'
# 返回值 dp[n]
# 优化空间复杂度
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == '0':
            return 0
        n = len(s)
        f0, f1 = 1, 1
        for i in range(1, n):
            f0, f1 = (f1,
                      (f1 if s[i] != '0' else 0)
                      + (f0 if 10 <= int(s[i - 1:i + 1]) <= 26 else 0))
        return f1


# 定义子问题
# f(i)为s[:i]的字符串有多少种解码方法
# f(i) = f(i-1) if s[i] != 0
#      + f(i-2) if int(s[i-i:i+1]) 在10到26之间
# 初始化和边界条件
# f(2) = ..
# f(1) = 0 if s[0] == '0' else 1
# f(0) = 1
# 返回值
# f(n)
# 优化复杂度
# 我们只需要两个值代表i-1和i-2即可
class Solution:
    def numDecodings(self, s: str) -> int:
        f0, f1 = 1, 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            if f1 == 0:
                return 0
            f0, f1 = (
                f1,
                (0 if s[i] == '0' else f1)
                + (f0 if 10 <= int(s[i - 1:i + 1]) <= 26 else 0)
            )
        return f1


# 定义f(i)为s[:i]有几种解法
# f(i) += f(i-1) if s[i] != '0'
# f(i) += f(i-2) if 10 <= s[i-1:i+1] <= 26
# 初始化
# f(0) = 1
# f(1) = 1 or 0
# 返回值f(n)
# 优化复杂地，只需要两个值
class Solution:
    def numDecodings(self, s: str) -> int:
        f0, f1 = 1, 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            if f1 == 0:
                return 0
            f0, f1 = (
                f1,
                (0 if s[i] == '0' else f1) +
                (f0 if 10 <= int(s[i - 1:i + 1]) <= 26 else 0)
            )
        return f1


def main():
    sol = Solution()

    s = "01"
    res = sol.numDecodings(s)
    print(res)

    s = "12"
    res = sol.numDecodings(s)
    print(res)

    s = "10"
    res = sol.numDecodings(s)
    print(res)

    s = "226"
    res = sol.numDecodings(s)
    print(res)


if __name__ == '__main__':
    main()
