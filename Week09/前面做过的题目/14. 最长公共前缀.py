# 14. 最长公共前缀.py
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


# 以下为自我练习
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = ""
        _min_len = float('inf')
        for s in strs:
            if len(s) < _min_len:
                _min_len = len(s)
                shortest = s

        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        _min_len = len(shortest)
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest


# Trie

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for o in strs:
                if o[i] != c:
                    return shortest[:i]
        return shortest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for other in strs:
                if other[i] != c:
                    return shortest[:i]
        return shortest


def main():
    s = Solution()

    strs = ["cas", "casdasd"]
    res = s.longestCommonPrefix(strs)
    print(res)


if __name__ == '__main__':
    main()
