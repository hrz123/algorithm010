# 2.py
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int],
                               boardingCost: int, runningCost: int) -> int:
        ans = 0
        res = 0
        p = 0
        w = 0
        i = 0
        for c in customers:
            i += 1
            w += c
            b = min(w, 4)
            w -= b
            p += b * boardingCost - runningCost
            if p > res:
                res = p
                ans = i
        while w:
            i += 1
            b = min(w, 4)
            w -= b
            p += b * boardingCost - runningCost
            if p > res:
                res = p
                ans = i
        return ans if ans else -1


def main():
    sol = Solution()
    customers = [8, 3]
    boardingCost = 5
    runningCost = 6
    res = sol.minOperationsMaxProfit(customers, boardingCost, runningCost)
    print(res)

    customers = [10, 10, 6, 4, 7]
    boardingCost = 3
    runningCost = 8
    res = sol.minOperationsMaxProfit(customers, boardingCost, runningCost)
    print(res)


if __name__ == '__main__':
    main()
