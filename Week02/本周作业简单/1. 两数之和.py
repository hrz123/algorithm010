# 1. 两数之和.py
from typing import List


# 1.暴力解法：枚举两个元素
# 时间复杂度：O(N^2)
# 空间复杂度：O(1)
# 2.使用hashmap记录已经访问的元素，这样只用遍历一遍。
# 就可以用O(1)的时间确定是否与前面的元素之和为target。
# 边遍历边添加。
# 时间复杂度：O(N)
# 空间复杂度：平均最坏都是O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], i]
            else:
                hashmap[target - num] = i

        return []


def main():
    pass


if __name__ == '__main__':
    main()
