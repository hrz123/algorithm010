# 1513. 仅含 1 的子串数.py
from collections import defaultdict


class Solution:
    def numSub(self, s: str) -> int:
        counter = defaultdict(int)
        cnt = 0
        for c in s:
            if c == '1':
                cnt += 1
            else:
                counter[cnt] += 1
                cnt = 0
        if cnt:
            counter[cnt] += 1
        res = 0
        print(counter)
        for c in counter:
            print(res)
            if counter[c] and c:
                res += c * (c + 1) // 2 * counter[c]
        return res % (10 ** 9 + 7)


def main():
    sol = Solution()
    s = "0110111"
    res = sol.numSub(s)
    print(res)


if __name__ == '__main__':
    main()
