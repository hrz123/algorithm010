# 922. 按奇偶排序数组 II.py
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        o, e = 1, 0
        for n in A:
            if n & 1:
                res[o] = n
                o += 2
            else:
                res[e] = n
                e += 2
        return res


# 以下为自我练习
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        o, e = 1, 0
        for a in A:
            if a & 1:
                res[o] = a
                o += 2
            else:
                res[e] = a
                e += 2
        return res


def main():
    pass


if __name__ == '__main__':
    main()
