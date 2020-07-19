# 5467. 找到最接近目标值的函数值.py
from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        nb = 10
        b1 = []
        b2 = []

        b1.append(arr[0])
        n = len(arr)

        res = abs(arr[0] - target)
        for i in range(1, n):
            x = arr[i]
            d = abs(x - target)
            b2 = [(d, x)]

            for y in b1:
                z = x & y
                d = abs(z - target)
                b2.append((d, z))

            b1 = []
            b2 = sorted(b2)
            res = min(res, b2[0][0])
            for _, y in b2[:nb]:
                b1.append(y)

        return res


def main():
    pass


if __name__ == '__main__':
    main()
