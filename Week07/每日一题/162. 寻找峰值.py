# 162. 寻找峰值.py
from typing import List


# 思路
# 定义高原数组
# array[l ..row]
# 如果array[l] > array[l - 1]
# 并且array[row] > array[row + 1]
# 我们就叫它高原数组
# 如果array退化为一个点，那么显然该店就是局部极大值点
# 题目中给出nums[start]!=arr[start+1]
# arr[-1] = arr[n] = -inf
# 算法描述
# 使用索引l, r指向数组首尾，根据定义该数组为高原数组
# 求中点mid = (l+row) // 2
# 如果nums[mid] > num[mid+1]
# 高原数组在左边，row = mid
# 如果nums[mid] < arr[mid+1]
# 高原数组在右边,l = mid + 1
# 最终l和r退化为一点
# 返回索引l
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


# 同理局部最小值
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < nums[mid + 1]:
                # 只需要改变符号方向
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


def main():
    sol = Solution()

    nums = [1, 2, 3, 1]
    res = sol.findPeakElement(nums)
    print(res)

    nums = [1, 2, 1, 3, 5, 6, 4]
    res = sol.findPeakElement(nums)
    print(res)


if __name__ == '__main__':
    main()
