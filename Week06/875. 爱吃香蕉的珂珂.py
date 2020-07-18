# 875. 爱吃香蕉的珂珂.py
from typing import List


# 二分法
# 速度的最低为1
# 速度的最高为数组的最大值
# 当当前速度所用时间比规定时间多时
# 说明速度满了，lo = mid + 1
# 否则，当前速度所有时间比规定时间小，或者等于当前时间
# 说明速度可以小于当前速度，或者就等于当前速度，hi = mid
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            time_used = self.__compute_time(piles, mid)
            if time_used > H:
                lo = mid + 1
            else:
                hi = mid
        return lo

    @staticmethod
    def __compute_time(piles, speed):
        res = 0
        for p in piles:
            res += (p - 1) // speed + 1
        return res


def main():
    sol = Solution()

    piles = [3, 6, 7, 11]
    H = 8
    res = sol.minEatingSpeed(piles, H)
    print(res)

    piles = [30, 11, 23, 4, 20]
    H = 5
    res = sol.minEatingSpeed(piles, H)
    print(res)

    piles = [30, 11, 23, 4, 20]
    H = 6
    res = sol.minEatingSpeed(piles, H)
    print(res)


if __name__ == '__main__':
    main()
