# 5471. 和为目标值的最大数目不重叠非空子数组数目.py
from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        pre = {0}

        p = 0
        for n in nums:
            p += n
            if p - target in pre:
                res += 1
                p = 0
                pre = {0}
            else:
                pre.add(p)

        return res


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        pre = {0}
        p = 0
        for n in nums:
            p += n
            if p - target in pre:
                res += 1
                pre = {0}
                p = 0
            else:
                pre.add(p)
        return res


# 以下为自我练习
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        pre = {0}
        res = 0
        p = 0
        for n in nums:
            p += n
            if p - target in pre:
                res += 1
                p = 0
                pre = {0}
            else:
                pre.add(p)
        return res


def main():
    sol = Solution()
    nums = [-1, 3, 5, 1, 4, 2, -9]
    target = 6
    res = sol.maxNonOverlapping(nums, target)
    print(res)

    nums = [-2, 6, 6, 3, 5, 4, 1, 2, 8]
    target = 10
    res = sol.maxNonOverlapping(nums, target)
    print(res)

    nums = [1, 1, 1, 1, 1]
    target = 2
    res = sol.maxNonOverlapping(nums, target)
    print(res)

    nums = [0, 0, 0]
    target = 0
    res = sol.maxNonOverlapping(nums, target)
    print(res)

    nums = [-5, 5, -4, 5, 4]
    target = 5
    res = sol.maxNonOverlapping(nums, target)
    print(res)


if __name__ == '__main__':
    main()
