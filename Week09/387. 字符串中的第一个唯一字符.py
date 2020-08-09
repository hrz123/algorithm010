# 387. 字符串中的第一个唯一字符.py
from collections import Counter


# brute force 两个嵌套循环，枚举所有字符，枚举i后面的所有字符（找重复）
# hashmap计数（hashmap O(1), treemap O(logn))
# 数组做hash表(256,ascii)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        counter = Counter(s)
        for i in range(n):
            if counter[s[i]] == 1:
                return i
        return -1


# O(N)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j and s[j] == s[i]:
                    break
            else:
                return i
        return -1


# O(N^2)

# 以下为自我练习
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
        return -1


def main():
    sol = Solution()

    s = "leetcode"
    res = sol.firstUniqChar(s)
    print(res)

    s = "loveleetcode"
    res = sol.firstUniqChar(s)
    print(res)

    s = "cc"
    res = sol.firstUniqChar(s)
    print(res)


if __name__ == '__main__':
    main()
