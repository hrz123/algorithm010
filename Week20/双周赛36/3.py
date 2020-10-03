# 3.py
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int],
                      colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res


def main():
    pass


if __name__ == '__main__':
    main()
