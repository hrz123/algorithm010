# 5504. 使数组和能被 P 整除.py
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total < p:
            return -1
        if total % p == 0:
            return 0
        mod = total % p
        pre = [0]
        _sum = 0
        n = len(nums)
        res = n
        for num in nums:
            _sum += num
            pre.append(_sum)
        hash_map = {}
        for i, _sum in enumerate(pre):
            tmp = _sum % p
            if tmp in hash_map:
                res = min(res, i - hash_map[tmp])
            hash_map[(_sum + mod) % p] = i
        return -1 if res == n else res


def main():
    sol = Solution()
    nums = [26, 19, 11, 14, 18, 4, 7, 1, 30, 23, 19, 8, 10, 6, 26, 3]
    p = 26
    res = sol.minSubarray(nums, p)
    print(res)

    nums = [4, 4, 2]
    p = 7
    res = sol.minSubarray(nums, p)
    print(res)


if __name__ == '__main__':
    main()
