# 26.删除排序数组中的重复项.py

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 使用双指针的方法，newTail 最新的尾部
        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1


def main():
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = s.removeDuplicates(nums)
    print(res)
    print(nums)

    nums = [1, 1, 2]
    res = s.removeDuplicates(nums)
    print(res)
    print(nums)

    nums = []
    res = s.removeDuplicates(nums)
    print(res)
    print(nums)

    nums = [2]
    res = s.removeDuplicates(nums)
    print(res)
    print(nums)

    nums = [1, 1]
    res = s.removeDuplicates(nums)
    print(res)
    print(nums)


if __name__ == '__main__':
    main()
