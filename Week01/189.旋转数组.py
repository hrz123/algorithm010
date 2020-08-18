# 189.旋转数组.py
import time
from typing import List


class Solution:
    # 这里使用了比较 pythonic 的解法，
    # 在其他语言中要使用 temp 数组将 arr[:n - k] 的元素存起来
    # 一个一个存的话还能保证 O(1) 空间复杂度
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]


class Solution1:
    # 这里使用了最本质的解法：三次反转
    # 第一段反转全部
    # 第二段反转 0 .. k - 1
    # 第三段反转 k .. n - 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


# 以下为自我练习
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        k %= len(nums)

        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(nums)
        k %= n

        nums[:] = nums[n - k:] + nums[:n - k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


def main():
    s = Solution()
    array = [1, 2, 3, 4, 5, 6, 7]
    nums = array
    k = 3
    start = time.perf_counter()
    for _ in range(1000000):
        s.rotate(nums, k)
    end = time.perf_counter()
    print(end - start)
    print(nums)

    s = Solution1()
    array = [1, 2, 3, 4, 5, 6, 7]
    nums = array
    start = time.perf_counter()
    for _ in range(1000000):
        s.rotate(nums, k)
    end = time.perf_counter()
    print(end - start)
    print(nums)


if __name__ == '__main__':
    main()
