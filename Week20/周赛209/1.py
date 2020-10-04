# 1.py
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            c = 0
            for num in nums:
                if num >= i:
                    c += 1
            if c == i:
                return i
        return -1


def main():
    sol = Solution()
    nums = [3, 5]
    res = sol.specialArray(nums)
    print(res)


if __name__ == '__main__':
    main()
