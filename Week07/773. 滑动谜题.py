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
#             for x, (start, j) in bq:
#                 for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#                     _i, _j = start + dx, j + dy
#                     if -1 < _i < 2 and -1 < _j < 3:
#                         new_x = list(map(list, x))
#                         new_x[start][j], new_x[_i][_j] = new_x[_i][_j], 0
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
#         for start in range(2):
#             for j in range(3):
#                 if board[start][j] == 0:
#                     return start, j


# 以下为自我练习
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = (
            (1, 3),
            (0, 2, 4),
            (1, 5),
            (0, 4),
            (1, 3, 5),
            (2, 4)
        )

        s = ""
        for row in board:
            for i in row:
                s += str(i)
        if s == "123450":
            return 0
        # 双向bfs
        bq, eq, nq, res, visited = {(s, s.index('0'))}, {
            ("123450", 5)}, set(), 0, set()

        while bq:
            visited |= bq
            res += 1
            for x, zero_idx in bq:
                for nxt_ind in moves[zero_idx]:
                    _x = list(x)
                    _x[zero_idx], _x[nxt_ind] = _x[nxt_ind], _x[zero_idx]
                    _x = ''.join(_x)
                    elem = (_x, nxt_ind)
                    if elem not in visited:
                        if elem in eq:
                            return res
                        nq.add(elem)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4)
        }
        s = ''.join(str(e) for row in board for e in row)
        if s == '123450':
            return 0
        bq, eq, nq, visited, res = {(s, s.index('0'))}, {('123450', 5)}, \
                                   set(), {(s, s.index('0')), ('123450', 5)}, 0
        while bq:
            res += 1
            for x, idx in bq:
                for y in moves[idx]:
                    _x, _idx = self.get_new_x(x, idx, y)
                    if (_x, _idx) in eq:
                        return res
                    if (_x, _idx) not in visited:
                        visited.add((_x, _idx))
                        nq.add((_x, _idx))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1

    def get_new_x(self, x, idx, y):
        x = list(x)
        x[idx], x[y] = x[y], x[idx]
        return ''.join(x), y


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join([str(i) for row in board for i in row])
        end = '123450'
        if start == end:
            return 0
        bq, eq, nq, res = {(start, start.index('0'))}, {(end, 5)}, set(), 0
        visited = set()
        moves = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4)
        }
        while bq:
            visited |= bq
            res += 1
            for x, ind in bq:
                for nid in moves[ind]:
                    to_list = list(x)
                    to_list[ind], to_list[nid] = to_list[nid], to_list[ind]
                    nx = ''.join(to_list)
                    if (nx, nid) not in visited:
                        if (nx, nid) in eq:
                            return res
                        nq.add((nx, nid))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join([str(i) for row in board for i in row])
        end = '123450'
        if start == end:
            return 0
        bq, eq, nq, res, visited = {(start, start.index('0'))}, {(end, 5)}, \
                                   set(), 0, set()
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        while bq:
            visited |= bq
            res += 1
            for x, ind in bq:
                for nid in moves[ind]:
                    to_li = list(x)
                    to_li[ind], to_li[nid] = to_li[nid], to_li[ind]
                    nx = ''.join(to_li)
                    if (nx, nid) not in visited:
                        if (nx, nid) in eq:
                            return res
                        nq.add((nx, nid))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join([str(i) for row in board for i in row])
        end = '123450'
        if start == end:
            return 0
        bq, eq, nq, res = {(start, start.index('0'))}, {(end, 5)}, set(), 0
        visited = set()
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        while bq:
            visited |= bq
            res += 1
            for x, ind in bq:
                for y in moves[ind]:
                    li = list(x)
                    li[ind], li[y] = li[y], li[ind]
                    nx = ''.join(li)
                    if (nx, y) not in visited:
                        if (nx, y) in eq:
                            return res
                        nq.add((nx, y))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(e) for row in board for e in row)
        if s == '123450':
            return 0
        bq, eq, nq, res = {(s, s.index('0'))}, {("123450", 5)}, set(), 0
        visited = set()
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        while bq:
            visited |= bq
            res += 1
            for s, ind in bq:
                for nid in moves[ind]:
                    li = list(s)
                    li[ind], li[nid] = li[nid], li[ind]
                    ns = ''.join(li)
                    if (ns, nid) not in visited:
                        if (ns, nid) in eq:
                            return res
                        nq.add((ns, nid))
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


def main():
    sol = Solution()

    board = [[1, 2, 3], [4, 5, 0]]
    res = sol.slidingPuzzle(board)
    print(res)

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
