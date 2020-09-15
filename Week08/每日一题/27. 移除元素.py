# 27. 移除元素.py
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == val:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        return i


# 以下为自我练
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == val:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == val:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums) - 1
        while i <= l:
            if nums[i] == val:
                nums[i], nums[l] = nums[l], nums[i]
                l -= 1
            else:
                i += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)
        while j < n:
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


def main():
    sol = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    res = sol.removeElement(nums, val)
    print(res)
    print(nums)


if __name__ == '__main__':
    main()
