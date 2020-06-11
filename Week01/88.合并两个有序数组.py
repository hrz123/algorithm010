# 88.合并两个有序数组.py

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 用i，j计数，节省循环中使用 m-1 和 n-1 计算索引
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1

        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = []
    n = 0
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0, 0, 0]
    m = 0
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == '__main__':
    main()
