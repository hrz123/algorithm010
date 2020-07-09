# 11. 盛最多水的容器.py
from typing import List


# 暴力
# O(n^2)的解决办法

# 左右指针
# l, r = 0, len(height) - 1
# s = min(height[l], height[r]) * (r - l)
# res = max(res, s)
# if l <= r:
# l += 1
# else:
# r -= 1
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


def main():
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    nums = [3, 1, 2]
    sol = Solution()
    res = sol.maxArea(nums)
    print(res)


if __name__ == '__main__':
    main()
