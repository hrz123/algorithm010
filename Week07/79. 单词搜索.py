# 79. 单词搜索.py
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs_search(i, j, pre, visited):
            if pre == word:
                return True
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i = i + dx
                _j = j + dy
                if -1 < _i < h and -1 < _j < w \
                        and (_i, _j) not in visited \
                        and len(pre) < len(word) \
                        and board[_i][_j] == word[len(pre)]:
                    if dfs_search(_i, _j, pre + word[len(pre)],
                                  visited | {(_i, _j)}):
                        return True

        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if dfs_search(i, j, word[0], {(i, j)}):
                        return True
        return False


# 以下为自我练习
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        n = len(word)

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if self.dfs(1, i, j, board, word, h, w, n, {(i, j)}):
                        return True
        return False

    def dfs(self, level, i, j, board, word, h, w, n, visited):
        if level == n:
            return True
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            _i, _j = i + dx, j + dy
            if -1 < _i < h and -1 < _j < w \
                    and (_i, _j) not in visited \
                    and board[_i][_j] == word[level]:
                if self.dfs(level + 1, _i, _j, board, word,
                            h, w, n, visited | {(_i, _j)}):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        n = len(word)

        def dfs(level, i, j, visited):
            if level == n:
                return True

            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and (_i, _j) not in visited \
                        and board[_i][_j] == word[level]:
                    if dfs(level + 1, _i, _j, visited | {(_i, _j)}):
                        return True
            return False

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if dfs(1, i, j, {(i, j)}):
                        return True
        return False


def main():
    sol = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    res = sol.exist(board, word)
    print(res)

    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    res = sol.exist(board, word)
    print(res)

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    res = sol.exist(board, word)
    print(res)


if __name__ == '__main__':
    main()
