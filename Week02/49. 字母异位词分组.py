# 49. 字母异位词分组.py
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sorted_s = self.bucket_sort(s)
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]

        return list(hashmap.values())

    def bucket_sort(self, string: str) -> str:
        arr = [0] * 26
        li = []
        for c in string:
            arr[ord(c) - ord('a')] += 1
        for i, e in enumerate(arr):
            li.append(chr(ord('a') + i) * e)

        return ''.join(li)


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


def main():
    pass


if __name__ == '__main__':
    main()
