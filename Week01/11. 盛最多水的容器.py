# 11. 盛最多水的容器.py
from typing import List


# 暴力
# O(n^2)的解决办法

# 左右指针
# l, row = 0, len(height) - 1
# s = min(height[l], height[row]) * (row - l)
# res = max(res, s)
# if l <= row:
# l += 1
# else:
# row -= 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            left = height[l]
            right = height[r]

            if left <= right:
                res = max(res, left * (r - l))
                l += 1
            else:
                res = max(res, right * (r - l))
                r -= 1

        return res


# 以下为自我练习
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            left, right = height[l], height[r]
            if left <= right:
                max_area = max(max_area, left * (r - l))
                l += 1
            else:
                max_area = max(max_area, right * (r - l))
                r -= 1
        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            w = r - l
            if height[l] > height[r]:
                res = max(res, height[r] * w)
                r -= 1
            else:
                res = max(res, height[l] * w)
                l += 1
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            left = height[l]
            right = height[r]
            if left < right:
                res = max(res, left * (r - l))
                l += 1
            else:
                res = max(res, right * (r - l))
                r -= 1
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                h = height[l]
                l += 1
            else:
                h = height[r]
                r -= 1
            res = max(res, h * (r - l + 1))
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l] * (r - l))
                l += 1
            else:
                res = max(res, height[r] * (r - l))
                r -= 1
        return res


def main():
    sol = Solution()

    nums = [3, 1, 2]
    res = sol.maxArea(nums)
    print(res)

    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = sol.maxArea(nums)
    print(res)


if __name__ == '__main__':
    main()
