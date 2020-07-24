# 1207. 独一无二的出现次数.py
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        count = [0] * len(arr)
        for c in counter.values():
            if count[c - 1] > 0:
                return False
            count[c - 1] += 1
        return True


def main():
    pass


if __name__ == '__main__':
    main()
