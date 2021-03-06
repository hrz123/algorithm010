# 88.合并两个有序数组.py

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 用i，j计数，节省循环中使用 n-1 和 m-1 计算索引
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


# 以下为自我练习
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1

        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[tail] = nums1[m]
                m -= 1
            else:
                nums1[tail] = nums2[n]
                n -= 1
            tail -= 1

        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        tail = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[tail] = nums1[i]
                i -= 1
            else:
                nums1[tail] = nums2[j]
                j -= 1
            tail -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[tail] = nums2[j]
                j -= 1
            else:
                nums1[tail] = nums1[i]
                i -= 1
            tail -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        for j in range(n - 1, -1, -1):
            while i >= 0 and nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            nums1[i + j + 1] = nums2[j]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        while j >= 0:
            while i >= 0 and nums1[i] >= nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            nums1[i + j + 1] = nums2[j]
            j -= 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        while j >= 0:
            while i >= 0 and nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            nums1[i + j + 1] = nums2[j]
            j -= 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        for j in range(n - 1, -1, -1):
            while i >= 0 and nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            nums1[i + j + 1] = nums2[j]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        for j in range(n - 1, -1, -1):
            while i >= 0 and nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            nums1[i + j + 1] = nums2[j]


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
