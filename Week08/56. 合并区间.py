# 56. 合并区间.py
from typing import List


# 思路
# 按照0索引的值对列表中的列表排序
# 遍历每一个区间，如果前一个区间的1索引位置大于等于后一个区间的0索引位置
# 合并这两个区间，否则，看下一对区间
# 排序使用什么算法
# 值没有范围，快排最好，可以使用系统的，可以自己写快排
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        n = len(intervals)
        self.quickSort(intervals, 0, n - 1)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[len(res) - 1][1] < x:
                res.append([x, y])
            else:
                res[len(res) - 1][1] = max(res[len(res) - 1][1], y)
        return res

    def quickSort(self, intervals, l, r):
        if l >= r:
            return
        pivot = self.partition(intervals, l, r)
        self.quickSort(intervals, l, pivot - 1)
        self.quickSort(intervals, pivot + 1, r)

    def partition(self, intervals, l, r):
        pivot = r
        right = l
        for i in range(l, r):
            if intervals[i][0] < intervals[pivot][0]:
                intervals[i], intervals[right] = intervals[right], intervals[i]
                right += 1
        intervals[right], intervals[pivot] = intervals[pivot], intervals[right]
        return right


# 题解
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals = sorted(intervals)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals = sorted(intervals)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[len(res) - 1][1] < x:
                res.append([x, y])
            else:
                res[len(res) - 1][1] = max(y, res[len(res) - 1][1])
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # intervals = sorted(intervals, key=lambda x: x[0])
        intervals.sort()
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[len(res) - 1][1] < x:
                res.append([x, y])
            else:
                res[len(res) - 1][1] = max(y, res[len(res) - 1][1])
        return res


# 几个要点

# 先按照区间起始位置排序

# 遍历区间

# 如果结果数组是空的，或者当前区间的起始位置 > 结果数组中最后区间的终止位置，则不合并，
# 直接将当前区间加入结果数组。

# 反之将当前区间合并至结果数组的最后区间


# Java解法
# class Solution {
#     public int[][] merge(int[][] intervals) {
#         // 先按照区间起始位置排序
#         Arrays.sort(intervals, (v1, v2) -> v1[0] - v2[0]);
#         // 遍历区间
#         int[][] res = new int[intervals.length][2];
#         int idx = -1;
#         for (int[] interval: intervals) {
#             // 如果结果数组是空的，或者当前区间的起始位置 > 结果数组中最后区间的终止位置，
#             // 则不合并，直接将当前区间加入结果数组。
#             if (idx == -1 || interval[0] > res[idx][1]) {
#                 res[++idx] = interval;
#             } else {
#                 // 反之将当前区间合并至结果数组的最后区间
#                 res[idx][1] = Math.max(res[idx][1], interval[1]);
#             }
#         }
#         return Arrays.copyOf(res, idx + 1);
#     }
# }

# 以下为自我练习
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res


# 以下为自我练习
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort()
        res = []
        for x, y in intervals:
            if not res or res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(res[-1][1], y)
        return res


def main():
    sol = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = sol.merge(intervals)
    print(res)

    intervals = [[1, 4], [1, 5]]
    res = sol.merge(intervals)
    print(res)

    intervals = [[1, 4], [2, 3]]
    res = sol.merge(intervals)
    print(res)

    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    res = sol.merge(intervals)
    print(res)

    intervals = [[2, 3], [4, 6], [5, 7], [3, 4]]
    res = sol.merge(intervals)
    print(res)


if __name__ == '__main__':
    main()
