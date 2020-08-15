# 16. 最接近的三数之和.py
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('-inf')
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > target:
                    if abs(total - target) < abs(res - target):
                        res = total
                    k -= 1
                elif total < target:
                    if abs(total - target) < abs(res - target):
                        res = total
                    j += 1
                else:
                    return total
        return res


# 以下为自我练习
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum == target:
                    return target
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum > target:
                    r -= 1
                else:
                    l += 1
        return res


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum == target:
                    return target
                if abs(_sum - target) < abs(res - target):
                    res = _sum
                if _sum < target:
                    l += 1
                else:
                    r -= 1
        return res


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            t = target - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == t:
                    return target
                if total > t:
                    r -= 1
                else:
                    l += 1
                if abs(total - t) < abs(res - target):
                    res = total + nums[i]
        return res


def main():
    s = Solution()
    res = s.threeSumClosest([-1, 2, 1, -4], 1)
    print(res)


if __name__ == '__main__':
    main()
