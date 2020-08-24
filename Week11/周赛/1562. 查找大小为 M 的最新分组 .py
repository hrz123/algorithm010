# 1562. 查找大小为 M 的最新分组 .py
import bisect
from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        intervals = [(1, n)]
        for i, v in enumerate(reversed(arr)):
            loc = bisect.bisect(intervals, (v, n + 1))
            tmp = intervals[loc - 1]
            if v == tmp[0] == tmp[1]:
                intervals[loc - 1:loc] = []
                if tmp[1] - v == m:
                    return n - i - 1
            elif v == tmp[0]:
                intervals[loc - 1:loc] = [(v + 1, tmp[1])]
                if tmp[1] - v == m:
                    return n - i - 1
            elif v == tmp[1]:
                intervals[loc - 1:loc] = [(tmp[0], v - 1)]
                if v - tmp[0] == m:
                    return n - i - 1
            elif v > tmp[1]:
                continue
            else:
                intervals[loc - 1:loc] = [(tmp[0], v - 1), (v + 1, tmp[1])]
                if tmp[1] - v == m or v - tmp[0] == m:
                    return n - i - 1
        return -1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return len(arr)

        start = [0, len(arr) + 1]
        for i, t in enumerate(arr[::-1]):
            idt = bisect.bisect(start, t)
            start.insert(idt, t)
            if m == start[idt + 1] - start[idt] - 1 or m == start[idt] - start[
                idt - 1] - 1:
                return len(arr) - i - 1
        return -1


def main():
    sol = Solution()
    arr = [3, 1, 5, 4, 2]
    m = 2
    res = sol.findLatestStep(arr, m)
    print(res)

    arr = [1, 2]
    m = 1
    res = sol.findLatestStep(arr, m)
    print(res)

    arr = [3, 1, 2]
    m = 2
    res = sol.findLatestStep(arr, m)
    print(res)


if __name__ == '__main__':
    main()
