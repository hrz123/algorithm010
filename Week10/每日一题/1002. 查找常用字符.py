# 1002. 查找常用字符.py
from collections import defaultdict
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        req = defaultdict(int)
        for c in A[0]:
            req[c] += 1
        for i in range(1, len(A)):
            counter = defaultdict(int)
            for c in A[i]:
                if c in req:
                    counter[c] += 1
            for c in req:
                req[c] = min(req[c], counter[c])
        res = []
        for c in req:
            res.extend([c] * req[c])
        return res


class Solution:
    def commonChars(self, A):
        if not A:
            return []

        res = []
        for c in set(A[0]):
            count = [w.count(c) for w in A]
            s = c * min(count)  # 如果不是每个单词都有的字母，min(count)=0
            for a in s:
                res.append(a)
        return res


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        counter = defaultdict(int)
        for c in A[0]:
            counter[c] += 1
        for w in A[1:]:
            for c in counter:
                if w.count(c) < counter[c]:
                    counter[c] = w.count(c)
        res = []
        for c in counter:
            for _ in range(counter[c]):
                res.append(c)
        return res


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        counter = defaultdict(int)
        for c in A[0]:
            counter[c] += 1
        for w in A[1:]:
            for c in counter:
                if w.count(c) < counter[c]:
                    counter[c] = w.count(c)
        res = []
        for c in counter:
            for _ in range(counter[c]):
                res.append(c)
        return res


def main():
    sol = Solution()
    A = ["bella", "label", "roller"]
    res = sol.commonChars(A)
    print(res)


if __name__ == '__main__':
    main()
