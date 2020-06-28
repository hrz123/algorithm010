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


def main():
    s = Solution()
    res = s.threeSumClosest([-1, 2, 1, -4], 1)
    print(res)


if __name__ == '__main__':
    main()
