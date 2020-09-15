# 5508. 数的平方等于两数乘积的方法数.py
import bisect
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        res = 0

        def helper(nums1, nums2):

            nonlocal res
            for num1 in nums1:
                target = num1 * num1
                loc = bisect.bisect_left(nums2, num1)
                tmp = loc
                if loc < len(nums2) and nums2[loc] == num1:
                    while loc < len(nums2) and nums2[loc] == num1:
                        loc += 1
                    eq_len = loc - tmp
                    res += eq_len * (eq_len - 1) // 2
                l, r = tmp - 1, loc
                while l >= 0 and r < len(nums2):
                    if nums2[l] * nums2[r] == target:
                        left = 1
                        right = 1
                        l -= 1
                        while l >= 0 and nums2[l] == nums2[l + 1]:
                            left += 1
                            l -= 1
                        r += 1
                        while r < len(nums2) and nums2[r] == nums2[r - 1]:
                            right += 1
                            r += 1
                        res += left * right
                    elif nums2[l] * nums2[r] > target:
                        l -= 1
                    else:
                        r += 1

        helper(nums1, nums2)
        helper(nums2, nums1)
        return res


def main():
    sol = Solution()
    # nums1 = [7, 4]
    # nums2 = [5, 2, 8, 9]
    # res = sol.numTriplets(nums1, nums2)
    # print(res)
    #
    # nums1 = [1, 1]
    # nums2 = [1, 1, 1]
    # res = sol.numTriplets(nums1, nums2)
    # print(res)

    # nums1 = [1, 3, 1, 2]
    # nums2 = [2, 3, 5, 3, 2]
    # res = sol.numTriplets(nums1, nums2)
    # print(res)

    # nums1 = [3, 1, 2, 2]
    # nums2 = [1, 3, 4, 4]
    # res = sol.numTriplets(nums1, nums2)
    # print(res)

    nums1 = [4, 1, 4, 1, 12]
    nums2 = [3, 2, 5, 4]
    res = sol.numTriplets(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
