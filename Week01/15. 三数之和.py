# 15. 三数之和.py
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findNsum(l, r, N, target, result, results):
            # recursion terminator
            if r - l + 1 < N \
                    or N < 2 \
                    or target < nums[l] * N \
                    or target > nums[r] * N:
                return

            # process current row logic
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if target == s:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif target > s:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        # drill down
                        findNsum(i + 1, r, N - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums) - 1, 3, 0, [], results)
        return results


# 以下为自我练习
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or nums[l] * k > target \
                    or nums[r] * k < target:
                return
            if k == 2:
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif _sum < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result +
                                 [nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 3, 0, [], res)
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or nums[l] * k > target \
                    or nums[r] * k < target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i],
                                 result + [nums[i]], results)

        res = []
        nums.sort()
        findKSum(0, len(nums) - 1, 3, 0, [], res)
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or nums[l] * k > target \
                    or nums[r] * k < target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 3, 0, [], res)
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k or k < 2 or nums[l] * k > target or nums[r] * k < \
                    target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        res = []
        nums.sort()
        findKSum(0, len(nums) - 1, 3, 0, [], res)
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k or k < 2 or nums[l] * k > target or nums[r] * k < \
                    target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        res = []
        nums.sort()
        findKSum(0, len(nums) - 1, 3, 0, [], res)
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k or k < 2 or nums[l] * k > target or nums[r] * k \
                    < target:
                return
            if k == 2:
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r - k + 2):
                    if i == l or nums[i] != nums[i - 1]:
                        findKSum(i + 1, r, k - 1, target - nums[i], result + [
                            nums[i]], results)

        nums.sort()
        res = []
        findKSum(0, len(nums) - 1, 3, 0, [], res)
        return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    res = sol.threeSum(nums)
    print(res)


if __name__ == '__main__':
    main()
