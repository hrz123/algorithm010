# 1.py

class Solution:
    def maxDepth(self, s: str) -> int:
        cur = 0
        res = 0
        for c in s:
            if c == '(':
                cur += 1
                res = max(res, cur)
            elif c == ')':
                cur -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
