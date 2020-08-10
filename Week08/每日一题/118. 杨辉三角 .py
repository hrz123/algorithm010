# 118. 杨辉三角 .py
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        r = []
        for i in range(numRows):
            nr = r + [1]
            for j in range(1, i):
                nr[j] = r[j - 1] + r[j]
            res.append(nr)
            r = nr
        return res


# 以下为自我练习
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        r = []
        for i in range(numRows):
            nr = r + [1]
            for j in range(1, i):
                nr[j] += r[j - 1]
            res.append(nr)
            r = nr
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = []
        res = []
        for i in range(numRows):
            nr = r + [1]
            for j in range(1, i):
                nr[j] += r[j - 1]
            res.append(nr)
            r = nr
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = []
        res = []
        for i in range(numRows):
            nr = r + [1]
            for j in range(1, i):
                nr[j] += r[j - 1]
            res.append(nr)
            r = nr
        return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = []
        res = []
        for i in range(numRows):
            nr = r + [1]
            for j in range(1, i):
                nr[j] += r[j - 1]
            res.append(nr)
            r = nr
        return res


def main():
    sol = Solution()
    res = sol.generate(5)
    print(res)


if __name__ == '__main__':
    main()
