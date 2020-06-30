# 51. N皇后.py
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []

        self.result = []
        # 之前皇后所攻击的位置
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n, 0, [])

        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # recursion terminator
        if row >= n:
            self.result.append(cur_state)
            return
            # current level logic
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in \
                    self.na:
                continue
                # update the flags
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            # reverse states
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))

        return [board[i:i + n] for i in range(0, len(board), n)]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            row = len(queens)
            if row == n:
                result.append(queens)
                return None
            for col in range(n):
                if col not in queens and \
                        row - col not in xy_dif and \
                        row + col not in xy_sum:
                    xy_dif.add(row - col)
                    xy_sum.add(row + col)
                    DFS(queens + [col], xy_dif, xy_sum)
                    xy_dif.remove(row - col)
                    xy_sum.remove(row + col)

        result = []
        DFS([], set(), set())
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol]
                for sol in result]


def main():
    pass


if __name__ == '__main__':
    main()
