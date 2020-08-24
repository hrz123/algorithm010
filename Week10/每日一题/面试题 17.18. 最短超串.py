# 面试题 17.18. 最短超串.py
from collections import defaultdict
from typing import List


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        m, n = len(big), len(small)
        counter = defaultdict(int)
        for num in small:
            counter[num] += 1
        left, size = 0, m + 1
        l, r = 0, 0
        while r < m:
            tmp = big[r]
            r += 1
            if counter[tmp] > 0:
                n -= 1
            counter[tmp] -= 1
            while n == 0:
                if r - l < size:
                    size = r - l
                    left = l
                if counter[big[l]] == 0:
                    n += 1
                counter[big[l]] += 1
                l += 1
        return [] if size == m + 1 else [left, left + size - 1]


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        m, n = len(big), len(small)
        if m < n:
            return []
        counter = defaultdict(int)
        for c in small:
            counter[c] += 1
        l, r = 0, 0
        size = m + 1
        left = 0
        while r < m:
            tmp = big[r]
            r += 1
            if counter[tmp] > 0:
                n -= 1
            counter[tmp] -= 1
            while n == 0:
                if r - l < size:
                    size = r - l
                    left = l
                if counter[big[l]] == 0:
                    n += 1
                counter[big[l]] += 1
                l += 1
        return [] if size == m + 1 else [left, left + size - 1]


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        m, n = len(big), len(small)
        if m < n:
            return []
        counter = defaultdict(int)
        for c in small:
            counter[c] += 1
        size = m + 1
        left = 0
        l, r = 0, 0
        while r < m:
            tmp = big[r]
            r += 1
            if counter[tmp] > 0:
                n -= 1
            counter[tmp] -= 1
            while n == 0:
                if r - l < size:
                    size = r - l
                    left = l
                if counter[big[l]] == 0:
                    n += 1
                counter[big[l]] += 1
                l += 1
        return [] if size == m + 1 else [left, left + size - 1]


def main():
    pass


if __name__ == '__main__':
    main()
