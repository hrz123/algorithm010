# 338. 比特位计数.py
from typing import List


# 子问题
# f(m)，n的二进制数中的1的数目，返回该数值
# 定义状态数组
# f(m) m 0..num
# 递推方程
# 我们知道 m&(m-1)是抹去了n的最后一个0的值
# 除了0以外，n的二进制表示至少有一个1
# 另外n&(m-1)一定小于n，计算f(m)之前f(m&(m-1))一定已经算过
# f(m) = f(m&(m-1)) + 1
# 初始化
# f(0) = 0
# 返回值
# [f(0), f(1), ..., f(num)]
# 也就是dp数组
# 优化空间复杂度
# 无法优化
class Solution:
    def countBits(self, num: int) -> List[int]:
        f = [0] * (num + 1)
        for i in range(1, num + 1):
            f[i] = f[i & (i - 1)] + 1
        return f


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp


class Solution:
    def countBits(self, num: int) -> List[int]:
        f = [0] * (num + 1)
        for i in range(1, num + 1):
            f[i] = f[i & (i - 1)] + 1
        return f


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & i - 1] + 1
        return dp


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1
        return dp


def main():
    sol = Solution()
    n = 2
    res = sol.countBits(n)
    print(res)


if __name__ == '__main__':
    main()
