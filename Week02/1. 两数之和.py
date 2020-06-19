# 1. 两数之和.py
from typing import List


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
