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
            # current row logic
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
                return
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


# 以下为自我练习
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def dfs(queens, xy_dif, xy_sum):
            row = len(queens)
            if row == n:
                result.append(queens)
                return
            for col in range(n):
                if col not in queens and row - col not in xy_dif and row + col \
                        not in xy_sum:
                    xy_dif.add(row - col)
                    xy_sum.add(row + col)
                    dfs(queens + [col], xy_dif, xy_sum)
                    xy_dif.remove(row - col)
                    xy_sum.remove(row + col)

        dfs([], set(), set())
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in
                result]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.__dfs([], set(), set(), result, n)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in s] for s in result]

    def __dfs(self, queens, xy_dif, xy_sum, result, n):
        # recursion terminator
        row = len(queens)
        if row == n:
            result.append(queens)
            return
        # process current row logic
        for col in range(n):
            rc_dif = row - col
            rc_sum = row + col
            if col not in queens and rc_dif not in xy_dif and rc_sum not in xy_sum:
                xy_dif.add(rc_dif)
                xy_sum.add(rc_sum)
                # drill down
                self.__dfs(queens + [col], xy_dif, xy_sum, result, n)
                # reverse current row status if needed
                xy_dif.remove(rc_dif)
                xy_sum.remove(rc_sum)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.__dfs(0, [], res, n, 0, 0)
        return [['.' * col + 'Q' + '.' * (n - col - 1) for col
                 in ans] for ans in res]

    def __dfs(self, row, ans, res, n, xy_sum, xy_dif):
        # recursion terminator
        if row == n:
            res.append(ans)
            return
        # process current row logic
        for col in range(n):
            if col not in ans \
                    and not (1 << col + row) & xy_sum \
                    and not (1 << col - row + n - 1) & xy_dif:
                # drill down
                self.__dfs(row + 1, ans + [col], res, n,
                           xy_sum + (1 << col + row),
                           xy_dif + (1 << col - row + n - 1))
        # reverse current row status if needed


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.__dfs(0, [], set(), set(), n, res)
        return [['.' * c + 'Q' + '.' * (n - c - 1) for c in sol] for sol in res]

    def __dfs(self, r, pre, xy_sum, xy_dif, n, res):
        if r == n:
            res.append(pre)
            return

        for c in range(n):
            if c not in pre and r + c not in xy_sum and r - c not in xy_dif:
                self.__dfs(r + 1, pre + [c], xy_sum | {r + c}, xy_dif | {
                    r - c}, n, res)


# 位运算
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.__dfs(0, [], 0, 0, 0, n, res)
        return [['.' * c + 'Q' + '.' * (n - c - 1) for c in sol] for sol in res]

    def __dfs(self, r, pre, y, xy_sum, xy_dif, n, res):
        if r == n:
            res.append(pre)
            return

        for c in range(n):
            s = 1 << (r + c)
            d = 1 << (r - c + n - 1)
            if not 1 << c & y and not s & xy_sum and not d & xy_dif:
                self.__dfs(r + 1, pre + [c], y + (1 << c), xy_sum + s,
                           xy_dif + d, n, res)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(0, n, 0, 0, [], res)
        return [['.' * i + "Q" + '.' * (n - i - 1) for i in sol] for sol in res]

    def dfs(self, row, n, xy_sum, xy_dif, col, res):
        if row == n:
            res.append(col)
            return
        for c in range(n):
            _sum, _dif = 1 << (row + c), 1 << (row - c + n - 1)
            if c not in col and not _sum & xy_sum and not _dif & xy_dif:
                self.dfs(row + 1, n, xy_sum + _sum, xy_dif + _dif, col + [c],
                         res)


# 位运算终极解法
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        size = (1 << n) - 1
        self.dfs(0, n, 0, 0, 0, [], size, res)
        return [['.' * i + "Q" + '.' * (n - i - 1) for i in sol] for sol in res]

    def dfs(self, row, n, col, pie, na, pre, size, res):
        if row == n:
            res.append([self.log2_minus_1(p) for p in pre])
            return
        bits = (~(col | pie | na)) & size
        while bits:
            p = bits & (-bits)
            # bits &= (bits - 1)
            bits -= p
            self.dfs(row + 1, n, col | p, (pie | p) << 1, (na | p) >> 1,
                     pre + [p], size, res)

    def log2_minus_1(self, p):
        res = -1
        while p:
            res += 1
            p >>= 1
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        size = (1 << n) - 1
        self.dfs(0, n, 0, 0, 0, size, [], res)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]

    def dfs(self, row, n, col, pie, na, size, pre, res):
        if row == n:
            res.append([self.log2_minus_one(p) for p in pre])
            return
        bits = (~(col | pie | na)) & size
        while bits:
            p = bits & (-bits)
            bits -= p
            self.dfs(row + 1, n, col | p, (pie | p) << 1, (na | p) >> 1, size,
                     pre + [p], res)

    def log2_minus_one(self, p):
        res = -1
        while p:
            res += 1
            p >>= 1
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        size = (1 << n) - 1
        self.dfs(0, n, 0, 0, 0, size, [], res)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]

    def dfs(self, row, n, col, pie, na, size, pre, res):
        if row == n:
            res.append([self.log2(p) for p in pre])
            return
        bits = (~(col | pie | na)) & size
        while bits:
            p = bits & (-bits)
            bits -= p
            self.dfs(row + 1, n, col | p, (pie | p) << 1, (na | p) >> 1,
                     size, pre + [p], res)

    def log2(self, p):
        res = -1
        while p:
            res += 1
            p >>= 1
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(0, n, 0, 0, 0, (1 << n) - 1, [], res)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]

    def dfs(self, row, n, col, pie, na, size, pre, res):
        if row == n:
            res.append([self.log2(p) for p in pre])
            return
        bits = (~(col | pie | na)) & size
        while bits:
            p = bits & (-bits)
            bits -= p
            self.dfs(row + 1, n, col | p, (pie | p) << 1, (na | p) >> 1,
                     size, pre + [p], res)

    def log2(self, p):
        res = -1
        while p:
            res += 1
            p >>= 1
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        mask = (1 << n) - 1
        self._dfs(0, n, 0, 0, 0, mask, [], res)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]

    def _dfs(self, row, n, col, pie, na, mask, pre, res):
        if row == n:
            res.append([self._log2(c) for c in pre])
            return
        bits = (~(col | pie | na)) & mask
        while bits:
            p = bits & (-bits)
            bits -= p
            self._dfs(row + 1, n, col | p, (pie | p) << 1, (na | p) >> 1, mask,
                      pre + [p], res)

    def _log2(self, c):
        res = -1
        while c:
            c >>= 1
            res += 1
        return res


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        mask = (1 << n) - 1
        self._dfs(0, n, 0, 0, 0, mask, [], res)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]

    def _dfs(self, row, n, col, pie, na, mask, pre, res):
        if row == n:
            res.append((c.bit_length() - 1 for c in pre))
            return
        bits = (~(col | pie | na)) & mask
        while bits:
            p = bits & (-bits)
            bits -= p
            self._dfs(row + 1, n, col | p, (pie | p) << 1, (na | p) >> 1, mask,
                      pre + [p], res)


def main():
    n = 4
    sol = Solution()
    res = sol.solveNQueens(n)
    print(res)


if __name__ == '__main__':
    main()
