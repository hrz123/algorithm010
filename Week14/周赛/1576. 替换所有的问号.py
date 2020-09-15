# 1576. 替换所有的问号.py
import string


class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                for c in string.ascii_lowercase:
                    if (i == 0 or s[i - 1] != c) and (
                            i == n - 1 or s[i + 1] != c):
                        s[i] = c
        return "".join(s)


def main():
    pass


if __name__ == '__main__':
    main()
