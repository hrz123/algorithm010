# 34. 在排序数组中查找元素的第一个和最后一个位置.py
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [0, 0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l < len(nums) and nums[l] == target:
            res[0] = l
        else:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            print(l, r)
            mid = l + ((r - l) >> 1) + 1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        res[1] = l
        return res


# 官方解法
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `arr` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `arr`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]


# 以下为自我练习
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        # 找到左侧
        left = self.findLeft(nums, 0, len(nums) - 1, target)
        if left == -1:
            return [-1, -1]
        right = self.findRight(nums, 0, len(nums) - 1, target)
        return [left, right]

    def findLeft(self, nums, l, r, target):
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1

    def findRight(self, nums, l, r, target):
        while l < r:
            mid = l + ((r - l) >> 1) + 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return l


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = self.extreme_insertion_index(nums, 0, n, target, True)
        if left == n or nums[left] != target:
            return [-1, -1]
        return [left,
                self.extreme_insertion_index(nums, 0, n, target, False) - 1]

    def extreme_insertion_index(self, nums, l, r, target, left):
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > target or (left and nums[mid] == target):
                r = mid
            else:
                l = mid + 1
        return l


# 定义n为数组长度，可以找到第一个满足右侧集合条件的位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(l, r, left):
            while l < r:
                mid = l + ((r - l) >> 1)
                if nums[mid] > target or (left and nums[mid] == target):
                    r = mid
                else:
                    l = mid + 1
            return l

        n = len(nums)
        left = binary_search(0, n, True)
        if left == n or nums[left] != target:
            return [-1, -1]
        return [left, binary_search(0, n, False) - 1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, left):
            l, r = 0, len(nums)
            while l < r:
                mid = l + ((r - l) >> 1)
                if nums[mid] > target or (left and nums[mid] == target):
                    r = mid
                else:
                    l = mid + 1
            return l

        left = binary_search(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, binary_search(nums, target, False) - 1]


def main():
    sol = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res = sol.searchRange(nums, target)
    print(res)

    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    res = sol.searchRange(nums, target)
    print(res)

    nums = []
    target = 0
    res = sol.searchRange(nums, target)
    print(res)

    nums = [1, 1]
    target = 1
    res = sol.searchRange(nums, target)
    print(res)

    nums = [1]
    target = 1
    res = sol.searchRange(nums, target)
    print(res)


if __name__ == '__main__':
    main()
