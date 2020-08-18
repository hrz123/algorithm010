# 1238. 循环码排列.py
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [0]
        head = 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | head)
            head <<= 1
        idx = res.index(start)
        res[:] = res[::-1]
        res[len(res) - idx:] = res[len(res) - idx:][::-1]
        res[:len(res) - idx] = res[:len(res) - idx:][::-1]
        return res


def main():
    sol = Solution()
    n = 2
    res = sol.circularPermutation(n, 3)
    print(res)


if __name__ == '__main__':
    main()
