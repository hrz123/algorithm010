# 1011. 在 D 天内送达包裹的能力.py
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        lo = 0
        hi = 0
        for w in weights:
            lo = lo if lo > w else w
            hi += w
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            count = 1
            total = 0
            for w in weights:
                total += w

                if total > mid:
                    count += 1
                    total = w
            if count > D:
                lo = mid + 1
            else:
                hi = mid
        return lo


# 以下为自我练习
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        hi = lo = 0
        for w in weights:
            hi += w
            lo = max(lo, w)
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            count = self._count(weights, mid)
            if count > D:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _count(self, weights, cap):
        count = 1
        _sum = 0
        for w in weights:
            _sum += w
            if _sum > cap:
                count += 1
                _sum = w
        return count


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = 0, 0
        for w in weights:
            lo = max(lo, w)
            hi += w
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self._count(weights, mid) > D:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _count(self, weights, cap):
        count = 1
        _sum = 0
        for w in weights:
            _sum += w
            if _sum > cap:
                count += 1
                _sum = w
        return count


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo, hi = 0, 0
        for w in weights:
            lo = max(lo, w)
            hi += w

        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self._count(weights, mid) > D:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def _count(self, weights, mid):
        c = 1
        p = 0
        for n in weights:
            p += n
            if p > mid:
                c += 1
                p = n
        return c


def main():
    sol = Solution()

    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D = 5
    res = sol.shipWithinDays(weights, D)
    print(res)

    weights = [3, 2, 2, 4, 1, 4]
    D = 3
    res = sol.shipWithinDays(weights, D)
    print(res)

    weights = [1, 2, 3, 1, 1]
    D = 4
    res = sol.shipWithinDays(weights, D)
    print(res)


if __name__ == '__main__':
    main()
