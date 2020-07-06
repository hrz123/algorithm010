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
# 和127不同的是，要找到最短的路径。因此，我们在bfs时需要构建一个搜索树
# 并且原路返回该树并恢复所有的最短路径。
# 所以我们不能一发现一个变换来的单词是结束单词就停止bfs，而应该继续在这一bfs层寻找
# 因为可能又不止一条最短路径。
# 我们仍需要排除之前我们寻找过的节点。同时，如果两个结点有一个相同的子节点。
# 我们需要将该子节点添加到两个节点的孩子数组上，因为我们要找到所有的有效路径。
# 所以不像常规的bfs，我们不能使用一个'seen'集合，更像用一个'explored'集合
# 否则，例如{x->z, y->z}, z不会被添加到y的孩子如果x首先被访问
# 并且z已经在x的搜索中
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        # tree用来还原路径
        tree, words, n = defaultdict(set), set(wordList), len(beginWord)

        if endWord not in words:
            return []

        # 用found增加循环的退出条件，因为这道题目不可以一找到就退出并返回
        found, q, nq = False, {beginWord}, set()

        while q and not found:
            words -= q
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

        # 还原轨迹的算法
        # 因为tree是有限的，bt的递归终止条件是x == endWord
        # 那么其实其他的结果最终会返回[]
        # 比如[hot, hat]
        # beginWord = hit
        # endWord = hot
        # 那么tree是{hit: {hot, hat}}
        # bt(hit)
        # bt(hit) == [[x] + rest for y in tree(x) for rest in bt(y)]
        #            [[hit] + rest for y in {hot, hat} for rest in bt(y)]]
        # bt(hot) == [[hot]]
        # bt(hat) == [[x] + rest for y in tree(x) for rest in bt(y)]
        #         == [[hat] + rest for y in set() for rest in bt(y)]
        #         == []
        # 函数返回x到endWord的所有路径，没有会返回[]
        def bt(x):
            return [[x]] if x == endWord \
                else [[x] + rest for y in tree[x] for rest in bt(y)]

        return bt(beginWord)


# 双向bfs
# bfs的时间复杂度是O(b^d)，b是分支因子，d是深度
# 所以如果我们用双向bfs，从开始和结束同时扩展，
# 分支因子会被大大减少。
# 实际时间上会减少。
class Solution(object):

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:

        tree, words, n = defaultdict(set), set(wordList), len(beginWord)

        if endWord not in words:
            return []

        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False

        while bq and not found:
            words -= bq
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
            # recursion terminator
            # process current level logic
            # drill down
            # reverse current level status if needed
            return [[x]] if x == endWord \
                else [[x] + rest for y in tree[x] for rest in bt(y)]

        print(tree)

        return bt(beginWord)


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    # beginWord = "hit"
    # endWord = "hot"
    # wordList = ["hot", "hat"]

    sol = Solution()
    res = sol.findLadders(beginWord, endWord, wordList)
    print(res)


if __name__ == '__main__':
    main()
