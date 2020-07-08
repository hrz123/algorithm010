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


# 以下为自我练习


# 使用双指针法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        new_tail = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = num
        return new_tail + 1


def main():
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    res = s.removeDuplicates(nums)
    assert res == 5
    assert nums == [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]

    nums = [1, 1, 2]
    res = s.removeDuplicates(nums)
    assert res == 2
    assert nums == [1, 2, 2]

    nums = []
    res = s.removeDuplicates(nums)
    assert res == 0
    assert nums == []

    nums = [2]
    res = s.removeDuplicates(nums)
    assert res == 1
    assert nums == [2]

    nums = [1, 1]
    res = s.removeDuplicates(nums)
    assert res == 1
    assert nums == [1, 1]


if __name__ == '__main__':
    main()
