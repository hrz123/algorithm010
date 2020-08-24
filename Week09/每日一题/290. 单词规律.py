# 290. 单词规律.py


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        values = [None] * 26
        used = set()
        i = 0
        for sub in s.split():
            idx = ord(pattern[i]) - ord('a')
            if values[idx]:
                if values[idx] != sub:
                    return False
            else:
                if sub in used:
                    return False
                values[idx] = sub
                used.add(sub)
            i += 1
        return True


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        m1 = {}
        m2 = {}
        s = str.split()
        if len(pattern) != len(s):
            return False
        for c, w in zip(pattern, s):
            if c in m1:
                if m1[c] != w:
                    return False
            else:
                m1[c] = w
            if w in m2:
                if m2[w] != c:
                    return False
            else:
                m2[w] = c
        return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        m1 = {}
        m2 = {}
        for c, w in zip(pattern, s):
            if c in m1:
                if m1[c] != w:
                    return False
            else:
                m1[c] = w
            if w in m2:
                if m2[w] != c:
                    return False
            else:
                m2[w] = c
        return True


class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s = s.split()
        if len(p) != len(s):
            return False
        m1 = {}
        m2 = {}
        for c1, c2 in zip(p, s):
            if c1 in m1:
                if m1[c1] != c2:
                    return False
            else:
                m1[c1] = c2
            if c2 in m2:
                if m2[c2] != c1:
                    return False
            else:
                m2[c2] = c1
        return True


def main():
    sol = Solution()

    p = "abba"
    s = "dog cat cat dog"
    res = sol.wordPattern(p, s)
    print(res)


if __name__ == '__main__':
    main()
