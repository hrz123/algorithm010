# 1561. 你可以获得的最大硬币数目 .py
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        target = n // 3
        c = 0
        res = 0
        for i in range(n - 2, -1, -2):
            res += piles[i]
            c += 1
            if c == target:
                return res


def main():
    pass


if __name__ == '__main__':
    main()
