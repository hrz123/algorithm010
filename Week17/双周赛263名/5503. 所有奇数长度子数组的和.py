# 5503. 所有奇数长度子数组的和.py
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        pre = [0]
        for num in arr:
            pre.append(pre[-1] + num)
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i + 1, n + 1, 2):
                res += pre[j] - pre[i]
        return res


def main():
    pass


if __name__ == '__main__':
    main()
