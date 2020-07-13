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


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sol = Solution()
    res = sol.intersect(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
