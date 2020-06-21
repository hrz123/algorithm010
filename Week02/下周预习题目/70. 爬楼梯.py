# 70. 爬楼梯.py

# 斐波那契数列
# 1.递归。+缓存降低时间复杂度。不加缓存为O(2^N)
# 加缓存为O(N)
# 空间复杂度为递归栈的大小。O(N)
# 2.动态规划
# dp[i] = dp[i-1] + dp[i-2]
# 时间复杂度为O(N)
# 空间复杂度：O(N)
# 可以再省一点空间，只用两个指针。
# 这是空间复杂度为O(1)
# 如果n有大小限制，可以通过预计算。做到时间复杂度O(1)。
# 空间复杂度O(N)
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(n - 2):
            a, b = b, a + b

        return b


def main():
    pass


if __name__ == '__main__':
    main()
