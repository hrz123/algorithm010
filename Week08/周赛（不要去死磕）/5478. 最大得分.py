# 5478. 最大得分.py
from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        t = []
        for i in nums1:
            t.append((i, 0))
        for i in nums2:
            t.append((i, 1))
        t = sorted(t)
        n = len(t)
        i = 0
        fp = [0, 0]
        while i < n:
            if i + 1 < n and t[i][0] == t[i + 1][0]:
                fp = [max(fp) + t[i][0]] * 2
                i += 2
            else:
                fp[t[i][1]] += t[i][0]
                i += 1
        return max(fp) % int(1e9 + 7)


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans1, ans2 = 0, 0
        for num in sorted(nums1 | nums2):
            if num in nums1 and num in nums2:
                ans1 = ans2 = max(ans1, ans2)
            if num in nums1:
                ans1 += num
            if num in nums2:
                ans2 += num
        return max(ans1, ans2) % int(1e9 + 7)


def main():
    sol = Solution()

    nums1 = [2, 4, 5, 8, 10]
    nums2 = [4, 6, 8, 9]
    res = sol.maxSum(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
