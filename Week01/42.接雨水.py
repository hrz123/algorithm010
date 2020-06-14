# 42.接雨水.py

from typing import List


# 暴力法
# 直接按问题描述进行。对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。

# 算法：
# 初始化 ans = 0
# 从左向右扫描数组：
#    初始化 max_Left = 0 和 max_right = 0
#    从当前元素向左扫描并更新：
#        max_left = max(max_left, height[j])
#    从当前元素向右扫描并更新：
#        max_right = max(max_right, height[j])
#    将min(max_left, max_right) - height[i] 累加到 ans

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)

        for i in range(1, size - 1):
            max_left = max_right = 0
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            for j in range(i, size):
                max_right = max(max_right, height[j])
            ans += min(max_left, max_right) - height[i]

        return ans


# 时间复杂度： O(n^2)
# 空间复杂度： O(1)

# leetcode 超出时间限制


# 双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        left = right = water = 0
        i, j = 0, len(height) - 1
        while i <= j:
            left, right = max(left, height[i]), max(right, height[j])
            while i <= j and height[i] <= left <= right:
                water += left - height[i]
                i += 1
            while i <= j and height[j] <= right <= left:
                water += right - height[j]
                j -= 1
        return water


def main():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    res = s.trap(heights)
    print(res)


if __name__ == '__main__':
    main()
