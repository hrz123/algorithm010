# 300. 最长上升子序列.py
from typing import List


# dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(dp[i], res)
        return res


# 贪心+二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
            else:
                l, r = 0, len(stack) - 1
                while l < r:
                    mid = l + ((r - l) >> 1)
                    if stack[mid] >= n:
                        r = mid
                    else:
                        l = mid + 1
                stack[l] = n
        return len(stack)


# 以下为自我练习
# 贪心+二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
            else:
                l, r = 0, len(stack) - 1
                while l < r:
                    mid = l + ((r - l) >> 1)
                    if stack[mid] >= n:
                        r = mid
                    else:
                        l = mid + 1
                stack[l] = n
        return len(stack)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
            else:
                l, r = 0, len(stack) - 1
                while l < r:
                    mid = l + ((r - l) >> 1)
                    if stack[mid] < n:
                        l = mid + 1
                    else:
                        r = mid
                stack[l] = n
        return len(stack)


def main():
    sol = Solution()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = sol.lengthOfLIS(nums)
    print(res)

    nums = [10, 9, 2, 5, 3, 4]
    res = sol.lengthOfLIS(nums)
    print(res)


if __name__ == '__main__':
    main()
