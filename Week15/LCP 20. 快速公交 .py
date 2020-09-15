# LCP 20. 快速公交 .py
import heapq
from functools import lru_cache
from typing import List


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int,
                        jump: List[int], cost: List[int]) -> int:
        import sys
        sys.setrecursionlimit(1000000000)
        # dp = [float('inf')] * min(jump) * target
        _max = min(jump) * target

        @lru_cache(None)
        def dfs(n):
            if n == 0:
                return 0
            if n == 1:
                return inc
            if n == _max:
                return float('inf')
            res = float('inf')
            res = min(res, dfs(n - 1) + inc)
            res = min(res, dfs(n + 1) + dec)
            for i, j in enumerate(jump):
                if n % j == 0:
                    res = min(res, dfs(n // j) + cost[i])
            return res

        return dfs(target)


# class Solution:
#     def busRapidTransit(self, target: int, inc: int, dec: int,
#                         jump: List[int], cost: List[int]) -> int:
# heap = [(0, 0)]
# while heap:
#     spend, pos = heapq.heappop(heap)
#     if pos == target:
#         return target
#     if pos != 0:
#         heapq.heappush(heap, (spend + dec, pos - 1))
#     heapq.heappush(heap, (spend + inc, pos + 1))
#     for j, c in zip(jump, cost):
#         heapq.heappush(heap, (spend + c, pos * j))


class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int,
                        jump: List[int], cost: List[int]) -> int:
        # import sys
        # sys.setrecursionlimit(1)

        @lru_cache(None)
        def dfs(n):
            res = inc * n
            if n == 1:
                return res
            for j, c in zip(jump, cost):
                div = n // j
                if div * j == n:
                    res = min(res, dfs(div) + c)
                    continue
                if div != 0:
                    res = min(res, dfs(div) + c + (n - div * j) * inc)
                res = min(res, dfs(div + 1) + c + (div * j + j - n) * dec)
            return res

        return dfs(target) % 1000000007


# class Solution:
#     def busRapidTransit(self, target: int, inc: int, dec: int,
#                         jump: List[int], cost: List[int]) -> int:
#         upper = max(target // j * j + j for j in jump)
#         dp = [0] + [10 ** 15] * upper


def main():
    sol = Solution()
    # a, b, c, d, e = (5,
    #                  5,
    #                  3,
    #                  [6],
    #                  [10])
    # res = sol.busRapidTransit(a, b, c, d, e)
    # print(res)

    a, b, c, d, e = (612,
                     4,
                     5,
                     [3, 6, 8, 11, 5, 10, 4],
                     [4, 7, 6, 3, 7, 6, 4])
    res = sol.busRapidTransit(a, b, c, d, e)
    print(res)


if __name__ == '__main__':
    main()
