# 905. 按奇偶排序数组.py
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        l, r = 0, n - 1
        for n in A:
            if n & 1:
                res[r] = n
                r -= 1
            else:
                res[l] = n
                l += 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
