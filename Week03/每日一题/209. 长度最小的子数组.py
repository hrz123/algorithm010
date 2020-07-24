# 209. 长度最小的子数组.py

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


# 以下为自我练习
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = end = 0
        total = 0
        n = len(nums)
        min_len = n + 1

        while end < n:
            total += nums[end]
            end += 1
            while total >= s:
                min_len = min(min_len, end - start)
                total -= nums[start]
                start += 1
        return 0 if min_len == n + 1 else min_len


def main():
    sol = Solution()

    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = sol.minSubArrayLen(s, nums)
    print(res)


if __name__ == '__main__':
    main()
