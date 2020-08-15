# 212. 单词搜索 II.py
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}  # 构造字典树
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre,
                   visited):  # (start,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
            if '#' in node:  # 已有字典树结束
                res.add(pre)  # 添加答案
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i + di, j + dj
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (
                        _i, _j) not in visited:  # 可继续搜索
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][_j],
                           visited | {(_i, _j)})  # dfs搜索

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:  # 可继续搜索
                    search(i, j, trie[board[i][j]], board[i][j],
                           {(i, j)})  # dfs搜索
        return list(res)


# 以下为自我练习
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre, visited):
            # start, j当前坐标，node当前trie结点，pre前面的字符串，visited已访问坐标
            if '#' in node:
                res.add(pre)
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and \
                        (_i, _j) not in visited:
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][_j],
                           visited | {(_i, _j)})

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})

        return list(res)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and (_i, _j) not in visited \
                        and board[_i][_j] in node:
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][
                        _j], visited | {(_i, _j)})

        res, h, w = set(), len(board), len(board[0])

        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []

        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and board[_i][_j] in node \
                        and (_i, _j) not in visited:
                    search(_i, _j, node[board[_i][_j]], pre + board[_i][_j],
                           visited | {(_i, _j)})

        res, h, w = set(), len(board), len(board[0])

        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = True

        def dfs(i, j, pre, node, visited):
            if '#' in node:
                res.add(pre)
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and (_i, _j) not in visited \
                        and board[_i][_j] in node:
                    dfs(_i, _j, pre + board[_i][_j],
                        node[board[_i][_j]], visited | {(_i, _j)})

        h, w = len(board), len(board[0])
        res = set()
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    dfs(i, j, board[i][j], trie[board[i][j]], {(i, j)})

        return list(res)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        trie = {}

        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = True

        h, w = len(board), len(board[0])
        res = set()
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    s = board[i][j]
                    self.dfs(i, j, s, trie[s], res, {(i, j)}, board, h, w)
        return list(res)

    def dfs(self, i, j, pre, node, res, visited, board, h, w):
        if '#' in node:
            res.add(pre)

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            _i, _j = i + dx, j + dy
            if -1 < _i < h and -1 < _j < w \
                    and (_i, _j) not in visited \
                    and board[_i][_j] in node:
                s = board[_i][_j]
                self.dfs(_i, _j, pre + s, node[s], res, visited | {(_i, _j)},
                         board, h, w)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = True
        res = set()
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    self.dfs(i, j, board[i][j], trie[board[i][j]], res, h, w,
                             board, {(i, j)})
        return list(res)

    def dfs(self, i, j, pre, node, res, h, w, board, visited):
        if '#' in node:
            res.add(pre)
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            _i, _j = i + dx, j + dy
            if -1 < _i < h and -1 < _j < w \
                    and (_i, _j) not in visited \
                    and board[_i][_j] in node:
                self.dfs(_i, _j, pre + board[_i][_j], node[board[_i][_j]],
                         res, h, w, board, visited | {(_i, _j)})


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        m, n = len(board), len(board[0])
        trie = {}
        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = True
        res = set()
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and (_i, _j) not in visited \
                        and board[_i][_j] in node:
                    c = board[_i][_j]
                    dfs(_i, _j, node[c], pre + c, visited | {(_i, _j)})

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})

        return list(res)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        trie = {}
        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = True
        m, n = len(board), len(board[0])
        res = set()
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        def dfs(i, j, node, pre):
            if '#' in node:
                res.add(pre)
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and (_i, _j) not in visited \
                        and board[_i][_j] in node:
                    visited.add((_i, _j))
                    dfs(_i, _j, node[board[_i][_j]], pre + board[_i][_j])
                    visited.remove((_i, _j))

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    visited.add((i, j))
                    dfs(i, j, trie[board[i][j]], board[i][j])
                    visited.remove((i, j))
        return list(res)


def main():
    sol = Solution()

    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['start', 'h', 'k', 'row'],
        ['start', 'f', 'l', 'v']
    ]
    res = sol.findWords(board, words)
    print(res)

    board = [["a", "a"]]
    words = ["a"]
    res = sol.findWords(board, words)
    print(res)


if __name__ == '__main__':
    main()
