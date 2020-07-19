# 1512. 好数对的数目.py
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = [0] * 100
        for n in nums:
            counter[n - 1] += 1

        res = 0
        for c in counter:
            if c > 1:
                res += c * (c - 1) // 2
        return res


def main():
    sol = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    res = sol.numIdenticalPairs(nums)
    print(res)


if __name__ == '__main__':
    main()
