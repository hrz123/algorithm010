# 37. 解数独.py
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        box = [set(range(1, 10)) for _ in range(9)]

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    box[i // 3 * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(level=0):
            if level == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[level]
            b = i // 3 * 3 + j // 3
            for val in row[i] & col[j] & box[b]:
                row[i].remove(val)
                col[j].remove(val)
                box[b].remove(val)
                board[i][j] = str(val)
                if backtrack(level + 1):
                    return True
                row[i].add(val)
                col[j].add(val)
                box[b].add(val)
            return False

        backtrack()


# 以下为自我练习
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        box = [set(range(1, 10)) for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    box[i // 3 * 3 + j // 3].remove(val)

        def backtrack(level=0):
            if level == len(empty):
                return True
            i, j = empty[level]
            b = i // 3 * 3 + j // 3
            for val in row[i] & col[j] & box[b]:
                board[i][j] = str(val)
                row[i].remove(val)
                col[j].remove(val)
                box[b].remove(val)
                if backtrack(level + 1):
                    return True
                board[i][j] = '.'
                row[i].add(val)
                col[j].add(val)
                box[b].add(val)
            return False

        backtrack()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        box = [set(range(1, 10)) for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    box[i // 3 * 3 + j // 3].remove(val)

        def backtrack(level=0):
            if level == len(empty):
                return True

            i, j = empty[level]
            b = i // 3 * 3 + j // 3
            for val in row[i] & col[j] & box[b]:
                board[i][j] = str(val)
                row[i].remove(val)
                col[j].remove(val)
                box[b].remove(val)
                if backtrack(level + 1):
                    return True
                board[i][j] = '.'
                row[i].add(val)
                col[j].add(val)
                box[b].add(val)
            return False

        backtrack()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        empty = []
        for i in range(9):
            for j in range(9):
                b = i // 3 * 3 + j // 3
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = int(board[i][j])
                    row[i].add(val)
                    col[j].add(val)
                    box[b].add(val)

        def backtrace(level=0):
            if level == len(empty):
                return True
            i, j = empty[level]
            b = i // 3 * 3 + j // 3
            for k in range(1, 10):
                if k not in row[i] and k not in col[j] and k not in box[b]:
                    board[i][j] = str(k)
                    row[i].add(k)
                    col[j].add(k)
                    box[b].add(k)
                    if backtrace(level + 1):
                        return True
                    board[i][j] = '.'
                    row[i].remove(k)
                    col[j].remove(k)
                    box[b].remove(k)
            return False

        backtrace()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    empty.append((i, j))
                else:
                    c = int(c)
                    b = i // 3 * 3 + j // 3
                    row[i].add(c)
                    col[j].add(c)
                    box[b].add(c)

        def backtrace(n=0):
            if n == len(empty):
                return True
            i, j = empty[n]
            b = i // 3 * 3 + j // 3
            for c in range(1, 10):
                if c not in row[i] and c not in col[j] and c not in box[b]:
                    board[i][j] = str(c)
                    row[i].add(c)
                    col[j].add(c)
                    box[b].add(c)
                    if backtrace(n + 1):
                        return True
                    board[i][j] = '.'
                    row[i].remove(c)
                    col[j].remove(c)
                    box[b].remove(c)
            return False

        backtrace()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.append((i, j))
                else:
                    b = i // 3 * 3 + j // 3
                    val = int(val)
                    row[i].add(val)
                    col[j].add(val)
                    box[b].add(val)

        def backtrace(level=0):
            if level == len(empty):
                return True
            i, j = empty[level]
            b = i // 3 * 3 + j // 3
            for c in range(1, 10):
                if c not in row[i] and c not in col[j] and c not in box[b]:
                    board[i][j] = str(c)
                    row[i].add(c)
                    col[j].add(c)
                    box[b].add(c)
                    if backtrace(level + 1):
                        return True
                    board[i][j] = '.'
                    row[i].remove(c)
                    col[j].remove(c)
                    box[b].remove(c)
            return False

        backtrace()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.append((i, j))
                else:
                    val = int(val)
                    b = i // 3 * 3 + j // 3
                    row[i].add(val)
                    col[j].add(val)
                    box[b].add(val)
        n = len(empty)

        def backtrace(level=0):
            if level == n:
                return True
            i, j = empty[level]
            b = i // 3 * 3 + j // 3
            for k in range(1, 10):
                if k not in row[i] and k not in col[j] and k not in box[b]:
                    board[i][j] = str(k)
                    row[i].add(k)
                    col[j].add(k)
                    box[b].add(k)
                    if backtrace(level + 1):
                        return True
                    board[i][j] = '.'
                    row[i].remove(k)
                    col[j].remove(k)
                    box[b].remove(k)
            return False

        backtrace()


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    b = i // 3 * 3 + j // 3
                    val = int(board[i][j])
                    row[i].add(val)
                    col[j].add(val)
                    box[b].add(val)
        n = len(empty)

        def backtrace(level=0):
            if level == n:
                return True
            i, j = empty[level]
            b = i // 3 * 3 + j // 3
            for k in range(1, 10):
                if k not in row[i] and k not in col[j] and k not in box[b]:
                    board[i][j] = str(k)
                    row[i].add(k)
                    col[j].add(k)
                    box[b].add(k)
                    if backtrace(level + 1):
                        return True
                    board[i][j] = '.'
                    row[i].remove(k)
                    col[j].remove(k)
                    box[b].remove(k)
            return False

        backtrace()


def main():
    sol = Solution()

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    sol.solveSudoku(board)
    print(board)


if __name__ == '__main__':
    main()
