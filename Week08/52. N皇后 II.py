# 52. N皇后 II.py


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self.count = 0

        self.dfs(n, 0, 0, 0, 0)
        return self.count

    def dfs(self, n, row, cols, pie, na):
        if row == n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits
            bits &= (bits - 1)
            self.dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)


# 位运算终极解法
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        res = 0
        size = (1 << n) - 1

        def dfs(row, col, pie, na):
            nonlocal res
            if row == n:
                res += 1
                return
            # 得到当前所有的空位
            bits = (~(col | pie | na)) & size
            while bits:
                p = bits & (-bits)
                # bits &= (bits - 1)
                bits -= p
                # | ^ 都可以
                dfs(row + 1, col | p, (pie | p) << 1, (na | p) >> 1)

        dfs(0, 0, 0, 0)
        return res


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        size = (1 << n) - 1

        def dfs(row, n, col, pie, na):
            nonlocal res
            if row == n:
                res += 1
                return
            bits = (~(col | pie | na)) & size
            while bits:
                p = bits & (-bits)
                bits -= p
                dfs(row + 1, n, col | p, (pie | p) << 1, (na | p) >> 1)

        dfs(0, n, 0, 0, 0)
        return res


class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        size = (1 << n) - 1

        def dfs(row, col, pie, na):
            nonlocal res
            if row == n:
                res += 1
                return
            bits = (~(col | pie | na)) & size
            while bits:
                p = bits & (-bits)
                bits -= p
                dfs(row + 1, col | p, (pie | p) << 1, (na | p) >> 1)

        dfs(0, 0, 0, 0)
        return res


def main():
    sol = Solution()

    n = 4
    res = sol.totalNQueens(n)
    print(res)


if __name__ == '__main__':
    main()
