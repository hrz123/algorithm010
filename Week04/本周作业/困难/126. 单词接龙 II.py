# 126. 单词接龙 II.py
from collections import defaultdict, deque
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
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        if endWord not in wordList:
            return 0

        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        queue_begin = deque([(beginWord, 1)])
        queue_end = deque([(endWord, 1)])

        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        ans = None

        while queue_begin and queue_end:

            ans = self.


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol = Solution()
    res = sol.findLadders(beginWord, endWord, wordList)
    print(res)


if __name__ == '__main__':
    main()
