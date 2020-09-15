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


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if self.dfs(0, word, i, j, {(i, j)}, h, w, board):
                        return True
        return False

    def dfs(self, level, word, i, j, visited, h, w, board):
        if level == len(word) - 1:
            return True
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            _i, _j = i + dx, j + dy
            if -1 < _i < h and -1 < _j < w \
                    and (_i, _j) not in visited \
                    and board[_i][_j] == word[level + 1]:
                if self.dfs(level + 1, word, _i, _j, visited | {(_i, _j)}, h, w,
                            board):
                    return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(level, i, j, visited):
            if level == len(word):
                return True
            c = word[level]
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n \
                        and board[_i][_j] == c \
                        and (_i, _j) not in visited:
                    if dfs(level + 1, _i, _j, visited | {(_i, _j)}):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(1, i, j, {(i, j)}):
                        return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(board), len(board[0])

        def backtrace(l, i, j, visited):
            if l == len(word):
                return True
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and (_i, _j) not in visited \
                        and board[_i][_j] == word[l]:
                    if backtrace(l + 1, _i, _j, visited | {(_i, _j)}):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrace(1, i, j, {(i, j)}):
                        return True
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        def dfs(l, i, j):
            if l == len(word):
                return True
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and (_i, _j) not in visited \
                        and board[_i][_j] == word[l]:
                    visited.add((_i, _j))
                    if dfs(l + 1, _i, _j):
                        return True
                    visited.remove((_i, _j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(1, i, j):
                        return True
                    visited.remove((i, j))
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        def dfs(l, i, j):
            if l == len(word):
                return True
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and (_i, _j) not in visited \
                        and board[_i][_j] == word[l]:
                    visited.add((_i, _j))
                    if dfs(l + 1, _i, _j):
                        return True
                    visited.remove((_i, _j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(1, i, j):
                        return True
                    visited.remove((i, j))
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        visited = set()
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        h, w = len(board), len(board[0])

        def dfs(level, i, j):
            if level == n:
                return True
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < h and -1 < _j < w and (_i, _j) not in visited \
                        and board[_i][_j] == word[level]:
                    visited.add((_i, _j))
                    if dfs(level + 1, _i, _j):
                        return True
                    visited.remove((_i, _j))
            return False

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(1, i, j):
                        return True
                    visited.remove((i, j))
        return False


class Solution:
    def exist(self, board: [List[List[int]]], word: str) -> bool:
        def dfs(level, i, j):
            if level == wl:
                return True
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and board[_i][_j] == word[
                    level] and (_i, _j) not in visited:
                    visited.add((_i, _j))
                    if dfs(level + 1, _i, _j):
                        return True
                    visited.remove((_i, _j))
            return False

        m, n = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        wl = len(word)
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(1, i, j):
                        return True
                    visited.remove((i, j))
        return False


class Solution:
    def exist(self, board: [List[List[int]]], word: str) -> bool:
        def dfs(level, i, j):
            if level == wl:
                return True
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and board[_i][_j] == word[
                    level] and (_i, _j) not in visited:
                    visited.add((_i, _j))
                    if dfs(level + 1, _i, _j):
                        return True
                    visited.remove((_i, _j))
            return False

        m, n = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        wl = len(word)
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(1, i, j):
                        return True
                    visited.remove((i, j))
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

    board = [["a"]]
    word = "a"
    res = sol.exist(board, word)
    print(res)


if __name__ == '__main__':
    main()
