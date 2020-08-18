# 126. 单词接龙 II.py
import string
from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:

        words = set(wordList)
        if endWord not in words:
            return []
        found, n, bq, eq, nq, rev, tree = False, len(beginWord), {beginWord}, {
            endWord}, set(), False, defaultdict(set)

        while bq and not found:
            # 去除环
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n)
                          for c in "qwertyuiopasdfghjklzxcvbnm"]:
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
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for
                                               rest in bt(y)]

        return bt(beginWord)


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        n, bq, eq, nq, rev, found, tree = len(beginWord), {beginWord}, \
                                          {endWord}, set(), False, False, \
                                          defaultdict(set)

        while bq and not found:
            words -= bq

            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
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


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        bq, eq, nq, n, found, rev, tree = {beginWord}, {endWord}, set(), \
                                          len(endWord), False, False, \
                                          defaultdict(set)
        while bq and not found:
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          string.ascii_lowercase]:
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


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        bq, eq, nq, n, found, rev, tree = {beginWord}, {endWord}, set(), \
                                          len(endWord), False, False, \
                                          defaultdict(set)
        while bq and not found:
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          string.ascii_lowercase]:
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
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for
                                               rest in bt(y)]

        return bt(beginWord)


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        bq, eq, nq, n, found, rev, tree = {beginWord}, {endWord}, set(), \
                                          len(beginWord), False, False, \
                                          defaultdict(set)
        while bq and not found:
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          string.ascii_lowercase]:
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


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        bq, eq, nq, n, found, rev, tree = {beginWord}, {endWord}, set(), \
                                          len(beginWord), False, False, \
                                          defaultdict(set)
        while bq and not found:
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          string.ascii_lowercase]:
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
    pass


if __name__ == '__main__':
    main()
