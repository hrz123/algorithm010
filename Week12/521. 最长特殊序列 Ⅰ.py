# 521. 最长特殊序列 Ⅰ.py


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


def main():
    pass


if __name__ == '__main__':
    main()
