# 983. 最低票价.py
import bisect
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


def main():
    sol = Solution()

    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    res = sol.mincostTickets(days, costs)
    print(res)


if __name__ == '__main__':
    main()
