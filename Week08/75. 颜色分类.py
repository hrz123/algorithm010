# 75. 颜色分类.py
from typing import List


# O(N), two pointers
# sort, O(nlogn)
# hash int[] counter, O(N), O(N), 额外花费内存空间

# 本问题被称为 荷兰国旗问题
# ，最初由 Edsger W. Dijkstra提出。Dijkstra牛逼
# 其主要思想是给每个数字设定一种颜色，并按照荷兰国旗颜色的顺序进行调整。


# 我们用三个指针（p0, p2 和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。
# 本解法的思路是沿着数组移动 curr 指针，若nums[curr] = 0，
# 则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p2]互换。

# 算法
# 初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.
# 初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.
# 初始化当前考虑的元素序号 ：curr = 0.
# 这里注意
# While curr <= p2 :
# 若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。
# 若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。
# 若 nums[curr] = 1 ：将指针curr右移。
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p2, cur = 0, n - 1, 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
            else:
                cur += 1


# 复杂度分析
# 时间复杂度 :由于对长度 NN的数组进行了一次遍历，时间复杂度为O(N)O(N) 。
# 空间复杂度 :由于只使用了常数空间，空间复杂度为O(1)O(1) 。


# 以下为自我练习
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0, p2, cur = 0, n - 1, 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2, cur = 0, len(nums) - 1, 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2, cur = 0, len(nums) - 1, 0

        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2, cur = 0, len(nums) - 1, 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2, cur = 0, len(nums) - 1, 0
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
                cur -= 1
            cur += 1


def main():
    sol = Solution()

    # nums = [2, 0, 2, 1, 1, 0]
    # sol.sortColors(nums)
    # print(nums)

    nums = [2, 0, 2, 1, 1, 0, 2, 1, 0, 0, 2, 1, 2, 0, 0]
    sol.sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()
