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


def main():
    pass


if __name__ == '__main__':
    main()
