# 119. 杨辉三角 II.py
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        for i in range(1, rowIndex + 1):
            r.append(0)
            for j in range(i, 0, -1):
                r[j] = r[j] + r[j - 1]
        return r


def main():
    sol = Solution()

    res = sol.getRow(5)
    print(res)


if __name__ == '__main__':
    main()
