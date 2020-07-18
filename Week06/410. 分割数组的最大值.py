# 410. 分割数组的最大值.py
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = 0
        right = 0
        for num in nums:
            left = left if left > num else num
            right += num
        while left < right:
            mid = left + ((right - left) >> 1)
            # 初始值必须是一
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    total = num
                    count += 1
            if count > m:
                left = mid + 1
            else:
                right = mid

        return left


def main():
    sol = Solution()

    nums = [7, 2, 5, 10, 8]
    m = 2
    res = sol.splitArray(nums, m)
    print(res)

    nums = [1, 3, 5]
    m = 2
    res = sol.splitArray(nums, m)
    print(res)


if __name__ == '__main__':
    main()
