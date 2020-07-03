# 529. 扫雷游戏.py
from typing import List


class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1, 1, 1, -1, -1]
        self.dy = [1, 0, -1, 0, 1, -1, -1, 1]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[
        List[str]]:
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


def main():
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]

    board = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
    click = [1, 2]

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

    sol = Solution()
    res = sol.updateBoard(board, click)
    assert res == expect
    print(res)


if __name__ == '__main__':
    main()
