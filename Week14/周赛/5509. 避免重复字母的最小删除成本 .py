# 5509. 避免重复字母的最小删除成本 .py
from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        _sum = 0
        _max = 0
        pre = None
        for ch, c in zip(s, cost):
            if ch == pre:
                _sum += c
                _max = max(_max, c)
            else:
                res += _sum - _max
                _sum = c
                _max = c
            pre = ch
        res += _sum - _max
        return res


def main():
    sol = Solution()
    s = "abbbabaaabbbbbbabbaaaabbabbababbababbbabababbbaaababbabbbbbaabaaabbbbaabbaaabaaababbbbbaabaaaaaaaaab"
    cost = [13, 18, 38, 34, 20, 36, 38, 5, 24, 9, 35, 34, 25, 48, 35, 9, 18, 40,
            48,
            12, 22, 18, 6, 7, 32, 12, 4, 39, 28, 28, 19, 21, 9, 20, 23, 40, 11,
            13, 7,
            1, 3, 40, 32, 14, 8, 46, 35, 45, 12, 21, 49, 4, 48, 40, 34, 29, 7,
            49, 43,
            16, 38, 15, 47, 44, 19, 18, 29, 49, 18, 2, 38, 9, 40, 1, 45, 6, 8,
            26, 15,
            30, 14, 23, 48, 27, 22, 41, 20, 6, 27, 25, 24, 25, 27, 41, 50, 27,
            6, 12,
            19, 19]
    res = sol.minCost(s, cost)
    print(res)
    s = "aaabbbabbbb"
    cost = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]
    res = sol.minCost(s, cost)
    print(res)
    assert res == 26


if __name__ == '__main__':
    main()
