# 5505. 所有排列中的最大和.py
from typing import List


class Solution:
    def isMagic(self, target: List[int]) -> bool:
        n = len(target)
        origin = [*range(1, n + 1)]
        for k in range(1, n + 1):
            clone = origin[:]
            start = 0
            while True:
                if start + 1 < n and clone[start + 1] != target[start]:
                    break
                self.step1(clone, start, n)
                if clone[start:start + k] != target[start:start + k]:
                    break
                start += k
                if start >= n:
                    return True
        return False

    def step1(self, arr, start, n):
        arr[start:] = [arr[i] for i in range(start + 1, n, 2)] + \
                      [arr[i] for i in range(start, n, 2)]


def main():
    sol = Solution()
    nums = [2, 4, 3, 1, 5]
    res = sol.isMagic(nums)
    print(res)
    nums = [5, 4, 3, 2, 1]
    res = sol.isMagic(nums)
    print(res)
    nums = [*range(1, 5001)]
    res = sol.isMagic(nums)
    print(res)


if __name__ == '__main__':
    main()
