# 126. 单词接龙 II.py
from collections import defaultdict
from typing import List


# 1. dfs，用level记录转换次数，用path记录路径，visited防止环
# 当小于目前最小次数时，更新最小次数，结果集重置，添加path
# 当等于目前最小次数时，结果集添加path
# 当大于目前最小次数时，继续
# 超出时间限制


# 构建一个字典
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        if endWord not in wordList:
            return []
        all_combo_dict = defaultdict(list)
        size = len(beginWord)

        for word in wordList:
            for i in range(size):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        minLevel = float('inf')
        res = []

        def dfs(level, word, endWord, path):
            # recursion terminator
            nonlocal minLevel
            nonlocal res
            if word == endWord:
                if level == minLevel:
                    res.append(path[:])
                elif level < minLevel:
                    minLevel = level
                    res = [path[:]]
                return
            # process current level logic
            for i in range(size):
                genericWord = word[:i] + '*' + word[i + 1:]
                new_words = all_combo_dict[genericWord]
                all_combo_dict[genericWord] = []

                for other_word in new_words:
                    path.append(other_word)
                    # drill down
                    dfs(level + 1, other_word, endWord, path)
                    # reverse current level status if needed
                    path.pop()
                all_combo_dict[genericWord] = new_words

        dfs(0, beginWord, endWord, [beginWord])
        return res


# bfs
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        tree, words, n = defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList:
            return []
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y == endWord:
                            found = True
                        else:
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()

        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x]
                                               for rest in bt(y)]

        return bt(beginWord)


# 双向bfs
class Solution(object):

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        tree, words, n = defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList:
            return []
        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in eq:
                            found = True
                        else:
                            nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x]
                                               for rest in bt(y)]

        return bt(beginWord)


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol = Solution()
    res = sol.findLadders(beginWord, endWord, wordList)
    print(res)


if __name__ == '__main__':
    main()
