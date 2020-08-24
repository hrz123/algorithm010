# 1563. 石子游戏 V.py
from functools import lru_cache
from typing import List


class Solution:
    def stoneGameV(self, a: List[int]) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l == r:
                return 0
            if l + 1 == r:
                return min(a[l], a[r])

            total = sum(a[i] for i in range(l, r + 1))
            left = 0
            ans = 0
            for i in range(l, r):
                left += a[i]
                right = total - left
                if left < right:
                    ans = max(ans, dfs(l, i) + left)
                elif left > right:
                    ans = max(ans, dfs(i + 1, r) + right)
                else:
                    ans = max(ans, max(dfs(l, i), dfs(i + 1, r)) + right)
            return ans

        n = len(a)
        return dfs(0, n - 1)


# 以下为自我练习
class Solution:
    def stoneGameV(self, a: List[int]) -> int:
        import functools
        @functools.lru_cache(None)
        def dfs(l, r):
            if l == r:
                return 0
            if l + 1 == r:
                return min(a[l], a[r])
            total = sum(a[l:r + 1])
            left = 0
            ans = 0
            for i in range(l, r):
                left += a[i]
                right = total - left
                if left < right:
                    ans = max(ans, dfs(l, i) + left)
                elif left > right:
                    ans = max(ans, dfs(i + 1, r) + right)
                else:
                    ans = max(ans, max(dfs(l, i), dfs(i + 1, r)) + left)
            return ans

        n = len(a)
        return dfs(0, n - 1)


class Solution:
    def stoneGameV(self, a: List[int]) -> int:
        import functools
        @functools.lru_cache(None)
        def dfs(l, r):
            if l == r:
                return 0
            if l + 1 == r:
                return min(a[l], a[r])
            total = sum(a[l:r + 1])
            left = 0
            ans = 0
            for i in range(l, r):
                left += a[i]
                right = total - left
                if left < right:
                    ans = max(ans, left + dfs(l, i))
                elif left > right:
                    ans = max(ans, right + dfs(i + 1, r))
                else:
                    ans = max(ans, max(dfs(l, i), dfs(i + 1, r)) + left)
            return ans

        n = len(a)
        return dfs(0, n - 1)


def main():
    sol = Solution()
    nums = [6, 2, 3, 4, 5, 5]
    res = sol.stoneGameV(nums)
    print(res)
    # a = 175251963
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    res = sol.stoneGameV(nums)
    print(res)
    nums = [9, 8, 2, 4, 6, 3, 5, 1, 7]
    res = sol.stoneGameV(nums)
    print(res)

    nums = [98, 77, 24, 49, 6, 12, 2, 44, 51, 96]
    res = sol.stoneGameV(nums)
    print(res)


if __name__ == '__main__':
    main()
