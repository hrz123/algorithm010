# 36. 有效的数独.py
from typing import List


# 遍历了三次，不是很好的
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # judge row
        for row in board:
            seen = set()
            for e in row:
                if e != '.' and e in seen:
                    return False
                seen.add(e)
        # judge pre
        for j in range(9):
            seen = set()
            for i in range(9):
                e = board[i][j]
                if e != '.' and e in seen:
                    return False
                seen.add(e)
        # judge small matrix
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        e = board[i][j]
                        if e != '.' and e in seen:
                            return False
                        seen.add(e)
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init data
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    val = int(val)
                    b = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    row[i][val] = row[i].get(val, 0) + 1
                    col[j][val] = col[j].get(val, 0) + 1
                    box[b][val] = box[b].get(val, 0) + 1

                    # check if this value has been already seen before
                    if row[i][val] > 1 or col[j][val] > 1 or box[b][val] > 1:
                        return False
        return True


# 以下为自我练习
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    val = int(val)
                    b = i // 3 * 3 + j // 3

                    row[i][val] = row[i].get(val, 0) + 1
                    col[j][val] = col[j].get(val, 0) + 1
                    box[b][val] = box[b].get(val, 0) + 1

                    if row[i][val] > 1 or col[j][val] > 1 or box[b][val] > 1:
                        return False
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    val = int(val)
                    b = i // 3 * 3 + j // 3
                    row[i][val] = row[i].get(val, 0) + 1
                    col[j][val] = col[j].get(val, 0) + 1
                    box[b][val] = box[b].get(val, 0) + 1

                    if row[i][val] > 1 or col[j][val] > 1 or box[b][val] > 1:
                        return False
        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    val = int(val)
                    b = i // 3 * 3 + j // 3
                    row[i][val] = row[i].get(val, 0) + 1
                    col[j][val] = col[j].get(val, 0) + 1
                    box[b][val] = box[b].get(val, 0) + 1

                    if row[i][val] > 1 or col[j][val] > 1 or box[b][val] > 1:
                        return False
        return True


def main():
    sol = Solution()

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    res = sol.isValidSudoku(board)
    print(res)

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
    res = sol.isValidSudoku(board)
    print(res)


if __name__ == '__main__':
    main()
