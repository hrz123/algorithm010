# 209. 长度最小的子数组.py
import bisect
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


# 思路，双指针问题
# 两个指针，一个指向数组左边，一个指向数组右边，左边最开始指向0，右边最后指向n-1
# 如果此时数组的元素和小于s，右边的指针向右移，加上右指针的值，一旦超过s，记录其长度与最小长度
# 超过了s，减去左指针的值，左指针右移，
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        _min_len = n + 1
        l = r = 0
        _sum = 0
        while r < n:
            _sum += nums[r]
            r += 1
            while _sum >= s:
                _min_len = min(_min_len, r - l)
                _sum -= nums[l]
                l += 1
        return 0 if _min_len == n + 1 else _min_len


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        total = 0
        res = n + 1
        while r < n:
            total += nums[r]
            r += 1
            while total >= s:
                res = min(res, r - l)
                total -= nums[l]
                l += 1
        return 0 if res == n + 1 else res


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]

        for i in range(n):
            target = sums[i] + s
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                ans = min(ans, bound - i)
        return 0 if ans == n + 1 else ans


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        res = n + 1
        total = 0
        while r < n:
            tmp = nums[r]
            r += 1
            total += tmp
            while total >= s:
                res = min(res, r - l)
                total -= nums[l]
                l += 1
        return 0 if res == n + 1 else res


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        res = n + 1
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        for i in range(n):
            target = pre[i + 1] - s
            l, r = 0, i
            while l <= r:
                mid = l + ((r - l) >> 1)
                if pre[mid] <= target:
                    res = min(res, i + 1 - mid)
                    l = mid + 1
                else:
                    r = mid - 1
        return 0 if res == n + 1 else res


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        res = n + 1
        total = 0
        while r < n:
            tmp = nums[r]
            r += 1
            total += tmp
            while total >= s:
                res = min(res, r - l)
                total -= nums[l]
                l += 1
        return 0 if res == n + 1 else res


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        l, r = 0, 0
        total = 0
        while r < n:
            tmp = nums[r]
            r += 1
            total += tmp
            while total >= s:
                if r - l < res:
                    res = r - l
                total -= nums[l]
                l += 1
        return 0 if res == n + 1 else res


def main():
    sol = Solution()

    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = sol.minSubArrayLen(s, nums)
    print(res)

    s = 11
    nums = [1, 2, 3, 4, 5]
    res = sol.minSubArrayLen(s, nums)
    print(res)

    s = 4
    nums = [1, 4, 4]
    res = sol.minSubArrayLen(s, nums)
    print(res)

    s = 15
    nums = [1, 2, 3, 4, 5]
    res = sol.minSubArrayLen(s, nums)
    print(res)


if __name__ == '__main__':
    main()
