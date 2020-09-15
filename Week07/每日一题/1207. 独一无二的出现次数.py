# 1207. 独一无二的出现次数.py
from collections import Counter, defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        count = [0] * len(arr)
        for c in counter.values():
            if count[c - 1] > 0:
                return False
            count[c - 1] += 1
        return True


# 计数排序
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = [0] * 2001
        for num in arr:
            counter[num + 1000] += 1
        occur = [0] * len(arr)
        for i in range(2001):
            if counter[i]:
                if occur[counter[i]] == 1:
                    return False
                occur[counter[i]] += 1
        return True


# 以下为自我练习
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = [0] * 2001
        for i in arr:
            count[1000 + i] += 1
        occur = [0] * len(arr)
        for i in range(2001):
            if count[i]:
                if occur[count[i]] == 1:
                    return False
                occur[count[i]] += 1
        return True


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occurred = [0] * len(arr)
        for c in count.values():
            if occurred[c]:
                return False
            occurred[c] += 1
        return True


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen = [False] * (len(arr) + 1)
        for c in counter.values():
            if seen[c]:
                return False
            seen[c] = True
        return True


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c1 = Counter(arr)
        c2 = Counter(c1.values())
        for k in c2:
            if c2[k] > 1:
                return False
        return True


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c1 = defaultdict(int)
        for num in arr:
            c1[num] += 1
        mem = set()
        for v in c1.values():
            if v in mem:
                return False
            mem.add(v)
        return True


def main():
    sol = Solution()

    nums = [1, 2, 2, 1, 1, 3]
    res = sol.uniqueOccurrences(nums)
    print(res)


if __name__ == '__main__':
    main()
