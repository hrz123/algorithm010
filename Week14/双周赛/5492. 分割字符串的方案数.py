# 5492. 分割字符串的方案数.py


class Solution:
    def numWays(self, s: str) -> int:
        one = 0
        for i in s:
            if i == '1':
                one += 1
        if one % 3 != 0:
            return 0
        one //= 3
        left = 0
        right = 0
        cnt = 0
        for i in s:
            if i == '1':
                cnt += 1
            if cnt == one:
                left += 1
        cnt = 0
        for i in s[::-1]:
            if i == '1':
                cnt += 1
            if cnt == one:
                right += 1
        if one == 0:
            return (len(s) - 1) * (len(s) - 2) // 2 % 1000000007
        return left * right % 1000000007


def main():
    sol = Solution()
    s = "10101"
    res = sol.numWays(s)
    print(res)


if __name__ == '__main__':
    main()
