# 680. 验证回文字符串 Ⅱ.py


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isValid(l + 1, r) or isValid(l, r - 1)
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isValid(l + 1, r) or isValid(l, r - 1)
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isValid(l + 1, r) or isValid(l, r - 1)
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return helper(l + 1, r) or helper(l, r - 1)
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return helper(l + 1, r) or helper(l, r - 1)
            l += 1
            r -= 1
        return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return helper(l + 1, r) or helper(l, r - 1)
            l += 1
            r -= 1
        return True


def main():
    sol = Solution()

    s = 'abca'
    res = sol.validPalindrome(s)
    print(res)

    s = 'abcda'
    res = sol.validPalindrome(s)
    print(res)


if __name__ == '__main__':
    main()
