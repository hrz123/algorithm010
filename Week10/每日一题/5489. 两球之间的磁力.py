# 5489. 两球之间的磁力.py
from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        lo, hi = 1, position[-1] - position[0]
        lo = min(position[i + 1] - position[i] for i in range(n - 1))
        while lo < hi:
            mid = lo + ((hi - lo) >> 1) + 1
            if self.count(position, mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        return lo

    def count(self, position, mid):
        c = 1
        p = position[0]
        for pos in position[1:]:
            if pos - p >= mid:
                c += 1
                p = pos
        return c


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        lo, hi = 1, position[-1] - position[0]
        lo = min(position[i + 1] - position[i] for i in range(n - 1))
        while lo < hi:
            mid = lo + ((hi - lo) >> 1) + 1
            if self.count(position, mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        return lo

    def count(self, position, mid):
        c = 1
        target = position[0] + mid
        for i in range(len(position) - 1):
            if position[i] < target <= position[i + 1]:
                c += 1
                target = position[i + 1] + mid
        return c


def main():
    sol = Solution()

    position = [1, 2, 3, 4, 7]
    m = 3
    res = sol.maxDistance(position, m)
    print(res)
    assert res == 3

    position = [5, 4, 3, 2, 1, 1000000000]
    m = 2
    res = sol.maxDistance(position, m)
    print(res)
    assert res == 999999999


if __name__ == '__main__':
    main()
