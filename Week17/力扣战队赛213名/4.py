# 4.py
import math
from collections import defaultdict
from functools import lru_cache


class Solution:
    def keyboard(self, k: int, n: int) -> int:
        mod = 1000000007
        count = (0,) * 26

        @lru_cache(None)
        def dfs(i, pre):
            if i == 0:
                return 1
            res = 0
            counter = defaultdict(int)
            for a in pre:
                counter[a] += 1
            for ind in range(26):
                if pre[ind] < k and pre[ind] in counter:
                    tmp = sorted(pre[:ind] + (pre[ind] + 1,) + pre[ind + 1:])
                    res += dfs(i - 1, tuple(tmp)) * counter[pre[ind]]
                    counter.pop(pre[ind])
            return res

        res = dfs(n, count)
        return res % mod

    # @lru_cache(None)
    # def helper(self, k, n, ava):
    #     if n <= 0:
    #         return 0
    #     if n == 1:
    #         return ava
    #     res = 0
    #     while ava:
    #         n -= k
    #         ava -= 1
    #         res += self.helper(k, n, ava)
    #     return res

    @lru_cache(None)
    def combine(self, n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def main():
    sol = Solution()
    res = sol.keyboard(1, 2)
    print(res)

    res = sol.keyboard(1, 1)
    print(res)

    res = sol.keyboard(2, 2)
    print(res)

    res = sol.keyboard(5, 130)
    print(res)


if __name__ == '__main__':
    main()
