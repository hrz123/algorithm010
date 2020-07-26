# 127. 单词接龙.py
import string
from collections import deque, defaultdict
from typing import List


# dfs解法
# 会超时
class Solution:
    def __init__(self):
        self.minLength = float('inf')

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        self.__dfs(0, beginWord, endWord, wordList, set())

        return 0 if self.minLength == float('inf') else self.minLength

    def __dfs(self, level, midWord, endWord, wordList, visited):
        # recursion terminator
        if midWord == endWord:
            self.minLength = min(self.minLength, level + 1)
            return
        # process current row logic
        for word in wordList:
            if word not in visited and self.__strDiff(word, midWord) == 1:
                visited.add(word)
                # drill down
                self.__dfs(level + 1, word, endWord, wordList, visited)
                # reverse current row status if needed
                visited.remove(word)

    def __strDiff(self, s1, s2):
        res = 0
        for i1, c1 in enumerate(s1):
            if c1 != s2[i1]:
                res += 1
        return res


# bfs解法
class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        lower_letters = "abcdefghijklmnopqrstuvwxyz"
        # 起始点算链条的开始
        res = 1
        deq = deque()
        deq.append(beginWord)
        visited = set(beginWord)
        while deq:
            size = len(deq)
            for _ in range(size):
                curWord = deq.popleft()
                if curWord == endWord:
                    return res
                for newWord in self.__showChanges(curWord, lower_letters):
                    if newWord in wordList and newWord not in visited:
                        deq.append(newWord)
                        visited.add(newWord)
            res += 1
        return 0

    def __showChanges(self, s, lower_letters):
        for i in range(len(s)):
            for ch in lower_letters:
                if ch != s[i]:
                    yield s[:i] + ch + s[i + 1:]


# 国际站bfs写法
# 使用neighbor words写法
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        def construct_dict(word_list):
            # 构建一个字典，示例key是a_cd，值是[abcd, aacd]
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            # bfs需要用到队列，visited防止环
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word == end:
                    return steps
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    neigh_words = dict_words.get(s, [])
                    # 遍历相差为1的字符串
                    for neigh in neigh_words:
                        if neigh not in visited:
                            queue.append((neigh, steps + 1))
                            visited.add(word)
                    # 这一句可以节省不少时间
                    dict_words[s] = []
            return 0

        d = construct_dict(wordList or {beginWord, endWord})
        return bfs_words(beginWord, endWord, d)


# 官方解法改进
# bfs
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words
                # which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = \
                    current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words
                # which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we findCompetitors what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also, mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


# 官方解法2改进：双向广度优先搜索
# 最快
# 中文注释
class Solution(object):
    def __init__(self):
        self.length = 0
        # 装载所有单词的组合的字典，通过一次改变一个字母。
        self.all_combo_dict = defaultdict(list)

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # 因为所有的单词都长度相同
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue_begin = deque([(beginWord, 1)])
        queue_end = deque([(endWord, 1)])

        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        while queue_begin and queue_end:

            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

            for word in self.all_combo_dict[intermediate_word]:
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return


# 时间复杂度：O(m*N)
# 空间复杂度：O(m*N)


# 单向bfs的另一种写法
# 更简洁
class Solution(object):

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> int:

        words, n = set(wordList), len(beginWord)

        if endWord not in words:
            return 0

        q, nq = {beginWord}, set()
        res = 1
        while q:
            res += 1
            words -= q
            for x in q:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y == endWord:
                            return res
                        else:
                            nq.add(y)
            q, nq = nq, set()

        return 0


# 双向bfs的写法
# 涉及到层级遍历的bfs可以用两个容器不停交换，达到层次遍历的效果
# 双向的增加一维从尾回来的队列
# 如果还要记录从begin的end的path，那么到end的时候要记录一个rev反序信息
class Solution(object):

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> int:

        words, n = set(wordList), len(beginWord)

        if endWord not in words:
            return 0

        bq, eq, nq = {beginWord}, {endWord}, set()
        res = 1
        while bq:
            res += 1
            # 通过这个操作去掉环
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return 0


# 以下为自我练习遍数
class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        words, n = set(wordList), len(beginWord)

        if endWord not in words:
            return 0

        bq, eq, nq = {beginWord}, {endWord}, set()

        res = 1

        while bq:
            res += 1
            words -= bq

            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
                    if y in words:
                        if y in eq:
                            return res
                        nq.add(y)

            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq

        return 0


# 单向bfs
class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        words, n = set(wordList), len(beginWord)

        if endWord not in words:
            return 0

        q, nq = {beginWord}, set()
        res = 1

        while q:
            res += 1
            # 去除环
            words -= q

            for x in q:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
                    if y in words:
                        if y == endWord:
                            return res
                        nq.add(y)
            q, nq = nq, set()

        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        n, bq, eq, nq = len(beginWord), {beginWord}, {endWord}, set()

        res = 0

        while bq:
            res += 1
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
                    if y in words:
                        if y in eq:
                            return res + 1
                        else:
                            nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq

        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        bq, eq, nq, n = {beginWord}, {endWord}, set(), len(endWord)

        res = 0
        while bq:
            words -= bq
            res += 1

            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
                    if y in words:
                        if y in eq:
                            return res + 1
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq

        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        bq, eq, nq, n = {beginWord}, {endWord}, set(), len(endWord)
        res = 1
        while bq:
            words -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
                    if y in words:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq

        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        bq, eq, nq, n, res = {beginWord}, {endWord}, set(), len(endWord), 1

        while bq:
            words -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          string.ascii_lowercase]:
                    if y in words:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return 0


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        bq, eq, nq, n, res = {beginWord}, {endWord}, set(), len(endWord), 1

        while bq:
            words -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
                    if y in words:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return 0


def main():
    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb",
                "kr", "ln",
                "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba",
                "to", "ra",
                "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
                "re", "or",
                "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr",
                "nb", "yb",
                "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li",
                "ha", "hz",
                "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
                "me", "mo",
                "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex",
                "pt", "io",
                "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq",
                "ye"]

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log2_and_minus_1", "cog"]

    sol = Solution()
    res = sol.ladderLength(beginWord, endWord, wordList)
    print(res)


if __name__ == '__main__':
    main()
