# 57. 插入区间.py
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        # init data
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1

            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        while idx < n and intervals[idx][0] < new_start:
            output.append(intervals[idx])
            idx += 1
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
        return output


def main():
    pass


if __name__ == '__main__':
    main()
