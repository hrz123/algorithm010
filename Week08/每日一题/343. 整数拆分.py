# 343. 整数拆分.py
import math


# 第一遍思路，对于任何一个数n可以拆分成2个数到最多n个数，其中拆分成n个数时乘积等于1，可以不考虑。
# 我们知道一个数平均拆分的时候，乘积是最大的（数学公式）。所以我们对所有这些情况尽量平局分。
# 对于2和3我们可以特殊处理，对于其他情况我们不希望乘积中出现1，因为出现1表示，
# 这个数和前面一个数的某个拆分的乘积相等，显示不是最大值。为了不出现1，我们选择最大遍历到n//2
# 时间复杂度：O(n)，假设乘方使用库函数是O(1)的。
# 空间复杂度：O(1)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        res = 2
        for i in range(2, n // 2 + 1):
            div, mod = divmod(n, i)
            res = max(res, math.pow(div, i - mod) * math.pow(div + 1, mod))
        return int(res)


# 动态规划
# 对于正整数n，当n大于等于2时，可以拆分成至少两个正整数的和。令k是拆分出的第一个正整数，
# 则剩下部分是n-k，n-k可以不继续拆分，或者继续拆分成至少两个正整数的和。
# 由于每个正整数对应的最大乘积取决于比它小的正整数对应的最大乘积，因此可以使用动态规划求解。
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)，n是数字大小
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


# 数学
# 4是唯一的一个拆分后的乘积最大值等于本身的数
# 3再拆分只有1，2和1，1，1两种，最大乘积是2，小于3，所以3不能拆分
# 而大于4的数拆分，都可以增大乘积
# 所以我们看尽量能凑成几个3
# 其中2和3我们特殊处理，因为它们一定要拆分，2要返回1，3要返回2，我们统一返回n-1即可
# 时间复杂度：O(1)
# 空间复杂度：O(1)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        div, mod = divmod(n, 3)
        if mod == 0:
            return 3 ** div
        if mod == 1:
            return 3 ** (div - 1) * 4
        return 3 ** div * 2


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        div, mod = divmod(n, 3)
        if not mod:
            return 3 ** div
        if mod == 1:
            return 3 ** (div - 1) * 4
        return 3 ** div * 2


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        div, mod = divmod(n, 3)
        if not mod:
            return 3 ** div
        if mod == 1:
            return 3 ** (div - 1) * 4
        return 3 ** div * 2


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        div, mod = divmod(n, 3)
        if mod == 0:
            return 3 ** div
        if mod == 1:
            return 3 ** (div - 1) * 4
        return 3 ** div * 2


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        div, mod = divmod(n, 3)
        if mod == 0:
            return 3 ** div
        if mod == 1:
            return 3 ** (div - 1) * 4
        return 3 ** div * 2


def main():
    sol = Solution()

    n = 2
    res = sol.integerBreak(n)
    print(res)

    n = 10
    res = sol.integerBreak(n)
    print(res)


if __name__ == '__main__':
    main()
