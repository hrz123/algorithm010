# 350. 两个数组的交集 II.py
from collections import defaultdict, Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counter2 = defaultdict(int)
        for num in nums2:
            counter2[num] += 1

        res = []
        for num in nums1:
            if counter2[num]:
                counter2[num] -= 1
                res.append(num)
        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counter2 = Counter(nums2)

        res = []
        for num in nums1:
            if counter2[num]:
                counter2[num] -= 1
                res.append(num)
        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        counter = Counter(nums1)
        for num in nums2:
            if counter[num]:
                counter[num] -= 1
                res.append(num)
        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counter = Counter(nums1)
        res = []
        for n in nums2:
            if counter[n]:
                res.append(n)
                counter[n] -= 1
        return res


# 解法1：使用计数器hashmap，时间复杂度O(n+m)的，空间复杂度需要建立一个m或n的哈希表
# 解法2：排序两个数组，然后使用两个指针，如果相等就都往后一步，
# 如果某一个指针的数字较小，往后移动一步，时间复杂度O(nlogn +mlogm)，双指针O(m)O(n)
# 空间复杂度O(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        counter = Counter(nums2)
        res = []
        for c in nums1:
            if counter[c]:
                res.append(c)
                counter[c] -= 1
        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counter = Counter(nums1)
        res = []
        for n in nums2:
            if counter[n] >= 1:
                res.append(n)
                counter[n] -= 1
        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        c1 = Counter(nums1)
        res = []
        for n in nums2:
            if c1[n] >= 1:
                res.append(n)
                c1[n] -= 1
        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        counter = defaultdict(int)
        for num in nums2:
            counter[num] += 1
        res = []
        for num in nums1:
            if counter[num]:
                res.append(num)
                counter[num] -= 1
        return res


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sol = Solution()
    res = sol.intersect(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
