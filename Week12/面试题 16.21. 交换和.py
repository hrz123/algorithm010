# 面试题 16.21. 交换和.py
from typing import List


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        s1, s2 = sum(array1), sum(array2)
        dif = s1 - s2
        if dif & 1:
            return []
        target = dif >> 1
        m, n = len(array1), len(array2)
        array1.sort()
        array2.sort()
        i, j = 0, 0
        while i < m and j < n:
            tmp = array1[i] - array2[j]
            if tmp == target:
                return [array1[i], array2[j]]
            if tmp > target:
                j += 1
            else:
                i += 1
        return []


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        dif = sum(array1) - sum(array2)
        if dif & 1:
            return []
        dif >>= 1
        s2 = set(array2)
        for a in array1:
            if a - dif in s2:
                return [a, a - dif]
        return []


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        dif = sum(array1) - sum(array2)
        if dif & 1:
            return []
        dif >>= 1
        s2 = set(array2)
        for a in array1:
            if a - dif in s2:
                return [a, a - dif]
        return []


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        dif = sum(array1) - sum(array2)
        if dif & 1:
            return []
        dif >>= 1
        s2 = set(array2)
        for a in array1:
            if a - dif in s2:
                return [a, a - dif]
        return []


def main():
    pass


if __name__ == '__main__':
    main()
