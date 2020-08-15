# 459. 重复的子字符串.py


# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


# 以下为自我练习
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)


def main():
    sol = Solution()

    s = "aba"
    res = sol.repeatedSubstringPattern(s)
    print(res)

    s = "a"
    res = sol.repeatedSubstringPattern(s)
    print(res)

    s = "aa"
    res = sol.repeatedSubstringPattern(s)
    print(res)


if __name__ == '__main__':
    main()
