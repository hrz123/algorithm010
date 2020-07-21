# 773. 滑动谜题.py
from typing import List


# dfs随便移动
# bfs 更快
# A*


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(c) for row in board for c in row)
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        if s == "123450":
            return 0
        bq, eq, nq, res, visited = {(s, s.index('0'))}, {
            ("123450", 5)}, set(), 0, set()

        while bq:
            res += 1
            visited |= bq
            for x, ind in bq:
                for n_ind in moves[ind]:
                    _x = list(x)
                    _x[ind], _x[n_ind] = _x[n_ind], _x[ind]
                    e = (''.join(_x), n_ind)
                    if e not in visited:
                        if e in eq:
                            return res
                        nq.add(e)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


# 第一遍解法，双向bfs
# class Solution:
#     def slidingPuzzle(self, board: List[List[int]]) -> int:
#         if board == [[1, 2, 3], [4, 5, 0]]:
#             return 0
#         zero_index = self.__find_zero_index(board)
#         bq, eq, nq, visited = {(tuple(map(tuple, board)), zero_index)}, \
#                               {(((1, 2, 3), (4, 5, 0)), (1, 2))}, set(), set()
#         res = 0
#         while bq:
#             res += 1
#             visited |= bq
#             for x, (i, j) in bq:
#                 for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#                     _i, _j = i + dx, j + dy
#                     if -1 < _i < 2 and -1 < _j < 3:
#                         new_x = list(map(list, x))
#                         new_x[i][j], new_x[_i][_j] = new_x[_i][_j], 0
#                         new_x = tuple(map(tuple, new_x))
#                         elem = (new_x, (_i, _j))
#                         if elem not in visited:
#                             if elem in eq:
#                                 return res
#                             nq.add(elem)
#             bq, nq = nq, set()
#             if len(bq) > len(eq):
#                 bq, eq = eq, bq
#         return -1
#
#     def __find_zero_index(self, board):
#         for i in range(2):
#             for j in range(3):
#                 if board[i][j] == 0:
#                     return i, j


def main():
    sol = Solution()

    board = [[1, 2, 3], [4, 0, 5]]
    res = sol.slidingPuzzle(board)
    print(res)

    board = [[1, 2, 3], [5, 4, 0]]
    res = sol.slidingPuzzle(board)
    print(res)

    board = [[4, 1, 2], [5, 0, 3]]
    res = sol.slidingPuzzle(board)
    print(res)

    board = [[3, 2, 4], [1, 5, 0]]
    res = sol.slidingPuzzle(board)
    print(res)


if __name__ == '__main__':
    main()
