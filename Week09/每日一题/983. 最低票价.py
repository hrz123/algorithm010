# 983. 最低票价.py
import bisect
from functools import lru_cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        memo = {}

        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            res = float('inf')
            res = min(res, dfs(i + 1) + costs[0])
            i7 = bisect.bisect(days, days[i] + 6)
            res = min(res, dfs(i7) + costs[1])
            i30 = bisect.bisect(days, days[i] + 29)
            res = min(res, dfs(i30) + costs[2])
            memo[i] = res
            return res

        return dfs(0)


# 以下为自我练习
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        # 这个函数定义为day[i]开始到结尾的最低消费
        @lru_cache(None)
        def backtrace(i):
            if i == n:
                return 0
            res = backtrace(i + 1) + costs[0]
            loc = bisect.bisect_left(days, days[i] + 7, i)
            res = min(res, backtrace(loc) + costs[1])
            loc = bisect.bisect_left(days, days[i] + 30, i)
            res = min(res, backtrace(loc) + costs[2])
            return res

        return backtrace(0)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            res = dp(i + 1) + costs[0]
            loc = bisect.bisect_left(days, days[i] + 7, i)
            res = min(res, dp(loc) + costs[1])
            loc = bisect.bisect_left(days, days[i] + 30, i)
            res = min(res, dp(loc) + costs[2])
            return res

        return dp(0)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        import functools
        @functools.lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            res = costs[0] + dp(i + 1)
            loc = bisect.bisect_left(days, days[i] + 7)
            res = min(res, costs[1] + dp(loc))
            loc = bisect.bisect_left(days, days[i] + 30)
            res = min(res, costs[2] + dp(loc))
            return res

        return dp(0)


def main():
    sol = Solution()

    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    res = sol.mincostTickets(days, costs)
    print(res)


if __name__ == '__main__':
    main()
