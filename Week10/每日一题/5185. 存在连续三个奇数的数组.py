# 5185. 存在连续三个奇数的数组.py
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n - 2):
            if arr[i] & 1 and arr[i + 1] & 1 and arr[i + 2] & 1:
                return True
        return False


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        r = 0
        n = len(arr)
        c = 0
        while r < n:
            tmp = arr[r]
            r += 1
            if tmp & 1:
                c += 1
                if c == 3:
                    return True
            else:
                c = 0
        return False


def main():
    pass


if __name__ == '__main__':
    main()
