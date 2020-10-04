# 3.py
from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]],
                      angle: int, location: List[int]) -> int:
        import math
        angle = angle / 360 * 2 * math.pi
        cnt = 0
        a = []
        for x, y in points:
            if x == location[0] and y == location[1]:
                cnt += 1
            else:
                xx, yy = x - location[0], y - location[1]
                a.append(math.atan2(yy, xx))
        a.sort()
        n = len(a)
        b = [x + math.pi * 2 for x in a]
        a += b
        j = 0

        ret = 0
        for i in range(n):
            while j < len(a):
                if a[j] - a[i] > angle:
                    break
                j += 1
            ret = max(ret, j - i)
        return ret + cnt


def main():
    pass


if __name__ == '__main__':
    main()
