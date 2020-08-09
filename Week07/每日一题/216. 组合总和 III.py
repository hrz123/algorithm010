# 216. 组合总和 III.py
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or target < (2 * l + k - 1) * k >> 1 \
                    or target > (2 * r - k + 1) * k >> 1:
                return
            if k == 2:
                while l < r:
                    _sum = l + r
                    if _sum == target:
                        results.append(result + [l, r])
                        l += 1
                    elif _sum > target:
                        r -= 1
                    else:
                        l += 1

            else:
                for i in range(l, r):
                    findKSum(i + 1, r, k - 1, target - i, result + [i], results)

        if k == 1:
            if 0 < n < 10:
                return [[n]]
        res = []
        findKSum(1, 9, k, n, [], res)
        return res


# 以下是自我练习
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def findKSum(l, r, k, target, result, results):
            if r - l + 1 < k \
                    or k < 2 \
                    or target < ((l << 1) + k - 1) * k >> 1 \
                    or target > ((r << 1) - k + 1) * k >> 1:
                return
            if k == 2:
                while l < r:
                    _sum = l + r
                    if _sum == target:
                        results.append(result + [l, r])
                        l += 1
                    elif _sum > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(l, r + 1):
                    findKSum(i + 1, r, k - 1, target - i, result + [i], results)

        res = []
        findKSum(1, 9, k, n, [], res)
        return res


def main():
    sol = Solution()
    k = 3
    n = 7
    res = sol.combinationSum3(k, n)
    print(res)

    k = 3
    n = 9
    res = sol.combinationSum3(k, n)
    print(res)


if __name__ == '__main__':
    main()
