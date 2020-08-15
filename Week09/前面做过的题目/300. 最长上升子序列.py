# 300. 最长上升子序列.py
import bisect
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


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
            l, r = 0, len(stack) - 1
            while l < r:
                mid = l + ((r - l) >> 1)
                if stack[mid] < n:
                    l = mid + 1
                else:
                    r = mid
            stack[l] = n
        return len(stack)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
            l, r = 0, len(stack) - 1
            while l < r:
                mid = l + ((r - l) >> 1)
                if stack[mid] < n:
                    l = mid + 1
                else:
                    r = mid
            stack[l] = n
        return len(stack)


# 定义f(start)为到i位置且必须包含i位置的最长上升子序列
# 递推方程
# f(start) = max(f(k) + 1, 1) for k 0..start-1 if a[start] > a[k]
# 初始化f(0) = 1
# 返回值，这些f(start)中的最大值
# 优化空间复杂度
# 无法优化
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            dp[i] = max(dp[k] + 1 if nums[i] > nums[k] else 1 for k in range(i))
            res = max(res, dp[i])
        return res


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


# 定义子问题
# s[:i]的最长上升子序列，如果结尾是s[i]
# 递推方程
# f(i) = f(k) + 1 如果a[i] > a[k] k 0..i-1
#      = 1 如果没有
# 初始化和边界条件
# f(0) = 1
# 返回值
# 这些值中的最大值
# 优化：无法
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            dp[i] = max(dp[k] + 1 if nums[k] < nums[i] else 1 for k in range(i))
            res = max(res, dp[i])
        return res


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
                loc = bisect.bisect_left(stack, n)
                stack[loc] = n
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
                loc = bisect.bisect_left(stack, n)
                stack[loc] = n
        return len(stack)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
            else:
                loc = bisect.bisect_left(stack, n)
                stack[loc] = n
        return len(stack)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for n in nums:
            if not stack or stack[-1] < n:
                stack.append(n)
            else:
                loc = bisect.bisect_left(stack, n)
                stack[loc] = n
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
                loc = bisect.bisect_left(stack, n)
                stack[loc] = n
        return len(stack)


def main():
    sol = Solution()

    nums = [10, 9, 2, 5, 3, 4]
    res = sol.lengthOfLIS(nums)
    print(res)
    # 3

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = sol.lengthOfLIS(nums)
    print(res)
    # 4

    nums = [10, 9, 2, 5, 3, 4]
    res = sol.lengthOfLIS(nums)
    print(res)
    # 3

    nums = []
    res = sol.lengthOfLIS(nums)
    print(res)
    assert res == 0


if __name__ == '__main__':
    main()
