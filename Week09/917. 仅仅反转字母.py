# 917. 仅仅反转字母.py


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l, r = 0, len(S) - 1
        s = list(S)
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        l, r = 0, len(S) - 1
        while l < r:
            while l < r and not S[l].isalpha():
                l += 1
            while l < r and not S[r].isalpha():
                r -= 1
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        return ''.join(S)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        l, r = 0, len(S) - 1
        while l < r:
            while l < r and not S[l].isalpha():
                l += 1
            while l < r and not S[r].isalpha():
                r -= 1
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        return ''.join(S)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalpha():
                l += 1
            while l < r and not s[r].isalpha():
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


def main():
    sol = Solution()

    s = "ab-cd"
    res = sol.reverseOnlyLetters(s)
    print(res)


if __name__ == '__main__':
    main()
