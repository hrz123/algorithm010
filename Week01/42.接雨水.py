# 42.接雨水.py

from typing import List


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
    pass


if __name__ == '__main__':
    main()
