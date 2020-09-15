# LCP 18. 早餐组合.py
import bisect
from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int],
                        x: int) -> int:
        staple.sort()
        drinks.sort()
        res = 0
        for s in staple:
            loc = bisect.bisect_right(drinks, x - s)
            res += loc - 1
        return res % 1000000007


def main():
    pass


if __name__ == '__main__':
    main()
