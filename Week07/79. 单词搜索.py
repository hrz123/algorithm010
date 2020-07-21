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


def main():
    sol = Solution()

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"

    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    res = sol.exist(board, word)
    print(res)


if __name__ == '__main__':
    main()
