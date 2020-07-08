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

            # process current level logic
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


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    res = sol.threeSum(nums)
    print(res)


if __name__ == '__main__':
    main()
