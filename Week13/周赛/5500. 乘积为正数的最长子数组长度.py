# 5500. 乘积为正数的最长子数组长度.py
from typing import List


# f(i, 01)为乘积为整数的最长子数组长度包括i
# if a[i] > 0:
# f(i, 0) = f(i-1, 0) + 1
# f(i, 1) = f(i-1, 1) + 1
# elif a[i] < 0:
# f(i, 0) = f(i-1, 1) + 1
# f(i, 1) = f(i-1, 0) + 1
# else:
# f(i, 0) = f(i, 1) = 0
# f(0, 0) = 0
# f(0, 1) = 0
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        f0 = f1 = 0
        if nums[0] > 0:
            f0, f1 = 1, 0
        elif nums[0] < 0:
            f0, f1 = 0, 1
        for num in nums[1:]:
            res = max(f0, res)
            if num > 0:
                f0, f1 = f0 + 1, f1 + 1 if f1 != 0 else 0
            elif num < 0:
                f0, f1 = f1 + 1 if f1 != 0 else 0, f0 + 1
            else:
                f0, f1 = 0, 0
        res = max(f0, res)
        return res


def main():
    sol = Solution()
    nums = [0, 1, -2, -3, -4]
    res = sol.getMaxLen(nums)
    print(res)


if __name__ == '__main__':
    main()
