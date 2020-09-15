# 5494. 统计所有可行路径.py
from functools import lru_cache
from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int,
                    finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        begin, end = locations[start], locations[finish]
        if abs(begin - end) > fuel:
            return 0
        n = len(locations)

        @lru_cache(None)
        def dfs(i, j, pre):
            if pre == 0:
                if i == j:
                    return 1
                return 0
            res = 0
            if i == j:
                res += 1
            for k in range(n):
                if k != i:
                    need = abs(locations[i] - locations[k])
                    if pre >= need:
                        res += dfs(k, j, pre - need)
            return res

        return dfs(start, finish, fuel) % mod


def main():
    sol = Solution()
    res = sol.countRoutes([4, 3, 1], 1, 0, 6)
    print(res)
    res = sol.countRoutes([1, 2, 3], 0, 2, 40)
    print(res)


if __name__ == '__main__':
    main()
