# 91. 解码方法.py


# 定义子问题
# s[:i]位置解码方法有多少种
# 定义状态数组
## dp(i) 0..n
# 递推方程
# f(i) = f(i-1) + f(i-2) if 0 < s[i-2:i] <= 26 and s[i-1] !=0
# f(i) = f(i-1)          if s[i-1] !=0
# f(i) = f(i-2)          if 0 < s[i-2:i] <= 26
# f(i) = 0               else
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
# 子问题为s[:i]的解码方法，i 0..n n = len(s)
# 定义状态数组
# f(i)
# 递推方程
# f(i) = f(i-1) + f(i-2)  if 10<=int(s[i-2:i])<=26 and s[i-1] != 0
#      = f(i-1)           elif s[i-1] != 0
#      = f(i-2)           elif 10<=int(s[i-2:i])<=26
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


def main():
    sol = Solution()

    s = "01"
    res = sol.numDecodings(s)
    print(res)

    s = "12"
    res = sol.numDecodings(s)
    print(res)

    s = "226"
    res = sol.numDecodings(s)
    print(res)


if __name__ == '__main__':
    main()
