# 529. 扫雷游戏.py
from typing import List


class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dy = [1, 0, -1, 0, 1, -1, -1, 1]

    def updateBoard(self, board: List[List[str]], click: List[int]) \
            -> List[List[str]]:
        self.__dfs(board, click[0], click[1])
        return board

    def __dfs(self, board, x, y):
        r = len(board)
        c = len(board[0])
        if x < 0 or x >= r or y < 0 or y >= c:
            return
        if board[x][y] == 'E':
            # 如果当前为E，才进行判断是否是要递归相邻节点
            board[x][y] = 'B'
            count = self.getAdjacentMines(board, x, y)
            if count == 0:
                # 如果为0，就进行递归
                for i in range(8):
                    self.__dfs(board, x + self.dx[i], y + self.dy[i])
            else:
                # 如果不为0，则更新当前结点的值为地雷数量
                board[x][y] = str(count)
        elif board[x][y] == 'M':
            board[x][y] = 'X'

    def getAdjacentMines(self, board, x, y):
        r = len(board)
        c = len(board[0])
        count = 0
        for i in range(8):
            newX = x + self.dx[i]
            newY = y + self.dy[i]
            if newX < 0 or newX >= r or newY < 0 or newY >= c:
                continue
            if board[newX][newY] == 'M':
                count += 1
        return count


# 国际站解法
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) \
            -> List[List[str]]:
        if not board:
            return []

        m, n = len(board), len(board[0])
        i, j = click[0], click[1]

        # If a mine ('M') is revealed, then the game is over - change it to 'X'.
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        # run dfs to reveal the board
        self.dfs(board, i, j, m, n)
        return board

    def dfs(self, board, i, j, m, n):
        if board[i][j] != 'E':
            return

        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1),
                      (-1, 1), (-1, 0)]

        mine_count = 0

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                mine_count += 1

        if mine_count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(mine_count)
            return

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(board, ni, nj, m, n)


# 以下为自我练习
class Solution:

    def __init__(self):
        self.dx = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dy = [1, 0, -1, 0, 1, -1, -1, 1]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[
        List[str]]:
        row = len(board)
        col = len(board[0])

        self.__dfs(board, row, col, click[0], click[1])

        return board

    def __dfs(self, board, row, col, x, y):
        if x < 0 or x >= row or y < 0 or y >= col:
            return
        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            # 如果当前为E，才进行判断是否是要递归相邻节点
            board[x][y] = 'B'
            # 获取当前临近地雷数量
            count = self.getAdjacentMines(board, row, col, x, y)
            if count == 0:
                # 如果为0，就进行递归
                for i in range(8):
                    self.__dfs(board, row, col, x + self.dx[i], y + self.dy[i])
            else:
                board[x][y] = str(count)

    def getAdjacentMines(self, board, row, col, x, y):
        count = 0
        for i in range(8):
            newx = x + self.dx[i]
            newy = y + self.dy[i]
            if 0 <= newx < row and 0 <= newy < col and board[newx][newy] == 'M':
                count += 1
        return count


class Solution:

    def __init__(self):
        self.dx = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dy = [1, 0, -1, 0, 1, -1, -1, 1]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[
        List[str]]:
        row, col = len(board), len(board[0])
        self.__dfs(board, click[0], click[1], row, col)
        return board

    def __dfs(self, board, x, y, row, col):
        if x < 0 or x >= row or y < 0 or y >= col:
            return
        if board[x][y] == 'E':
            board[x][y] = 'B'

            count = self.getAdjacentMines(board, x, y, row, col)

            if count == 0:
                for i in range(8):
                    self.__dfs(board, x + self.dx[i], y + self.dy[i], row, col)
            else:
                board[x][y] = str(count)
        elif board[x][y] == 'M':
            board[x][y] = 'X'

    def getAdjacentMines(self, board, x, y, row, col):
        count = 0
        for i in range(8):
            newx = x + self.dx[i]
            newy = y + self.dy[i]

            if 0 <= newx < row and 0 <= newy < col and board[newx][newy] == 'M':
                count += 1
        return count


class Solution:

    def __init__(self):
        self.dx = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dy = [1, 0, -1, 0, 1, -1, -1, 1]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[
        List[str]]:
        row, col = len(board), len(board[0])
        x, y = click
        self.__dfs(board, x, y, row, col)
        return board

    def __dfs(self, board, x, y, row, col):
        if x < 0 or x >= row or y < 0 or y >= col:
            return

        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            board[x][y] = 'B'

            count = self.getAdjacentMines(board, x, y, row, col)

            if count == 0:
                for i in range(8):
                    self.__dfs(board, x + self.dx[i], y + self.dy[i], row, col)
            else:
                board[x][y] = str(count)

    def getAdjacentMines(self, board, x, y, row, col):
        count = 0
        for i in range(8):
            newx, newy = x + self.dx[i], y + self.dy[i]

            if 0 <= newx < row and 0 <= newy < col and board[newx][newy] == 'M':
                count += 1
        return count


class Solution:
    def __init__(self):
        self.dx = (0, 1, 0, -1, 1, 1, -1, -1)
        self.dy = (1, 0, -1, 0, 1, -1, -1, 1)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[
        List[str]]:
        m, n = len(board), len(board[0])
        x, y = click
        self.__dfs(board, x, y, m, n)
        return board

    def __dfs(self, board, i, j, m, n):
        # recursion terminator
        if i < 0 or i >= m or j < 0 or j >= n:
            return

        if board[i][j] == 'E':
            mines = self.__getAdjacentMines(board, i, j, m, n)
            if mines == 0:
                board[i][j] = 'B'
                for k in range(8):
                    self.__dfs(board, i + self.dx[k], j + self.dy[k], m, n)
            else:
                board[i][j] = str(mines)

        elif board[i][j] == 'M':
            board[i][j] = 'X'

    def __getAdjacentMines(self, board, i, j, m, n):
        count = 0
        for k in range(8):
            if 0 <= i + self.dx[k] < m \
                    and 0 <= j + self.dy[k] < n \
                    and board[i + self.dx[k]][j + self.dy[k]] == 'M':
                count += 1
        return count


class Solution:
    def __init__(self):
        self.dx = (0, 1, 0, -1, 1, 1, -1, -1)
        self.dy = (1, 0, -1, 0, 1, -1, -1, 1)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[
        List[str]]:
        m = len(board)
        n = len(board[0])
        x, y = click
        self.__dfs_update(board, m, n, x, y)
        return board

    def __dfs_update(self, board, m, n, x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return
        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            mines = self.__get_adjacent_mines(board, m, n, x, y)
            if mines > 0:
                board[x][y] = str(mines)
            else:
                board[x][y] = 'B'
                for k in range(8):
                    self.__dfs_update(board, m, n, x + self.dx[k],
                                      y + self.dy[k])

    def __get_adjacent_mines(self, board, m, n, x, y):
        count = 0
        for k in range(8):
            x_new = x + self.dx[k]
            y_new = y + self.dy[k]
            if 0 <= x_new < m and 0 <= y_new < n and board[x_new][y_new] == 'M':
                count += 1
        return count


def main():
    sol = Solution()

    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]

    res = sol.updateBoard(board, click)
    print(res)

    board = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
    click = [1, 2]

    res = sol.updateBoard(board, click)
    print(res)

    board = [["E", "E", "E", "E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E", "E", "E", "M"],
             ["E", "E", "M", "E", "E", "E", "E", "E"],
             ["M", "E", "E", "E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E", "E", "E", "E"],
             ["E", "E", "M", "M", "E", "E", "E", "E"]]

    click = [0, 0]

    expect = [["B", "B", "B", "B", "B", "B", "1", "E"],
              ["B", "1", "1", "1", "B", "B", "1", "M"],
              ["1", "2", "M", "1", "B", "B", "1", "1"],
              ["M", "2", "1", "1", "B", "B", "B", "B"],
              ["1", "1", "B", "B", "B", "B", "B", "B"],
              ["B", "B", "B", "B", "B", "B", "B", "B"],
              ["B", "1", "2", "2", "1", "B", "B", "B"],
              ["B", "1", "M", "M", "1", "B", "B", "B"]]

    res = sol.updateBoard(board, click)
    print(res)
    assert res == expect
    print(res)


if __name__ == '__main__':
    main()
