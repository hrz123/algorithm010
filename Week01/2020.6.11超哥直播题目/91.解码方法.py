# 91.解码方法.py
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1

        cnt = 0

        if s[0] != '0':
            cnt += self.numDecodings(s[1:])
        if 10 <= int(s[0:2]) <= 26:
            cnt += self.numDecodings(s[2:])

        return cnt


def main():
    pass


if __name__ == '__main__':
    main()
