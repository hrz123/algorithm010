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
