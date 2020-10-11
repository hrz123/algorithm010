# 3.py


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalindrome(s):
            return s == s[::-1]

        if isPalindrome(a) and isPalindrome(b):
            return True
        n = len(a)

        if n & 1:
            l = r = n >> 1
        else:
            l, r = (n >> 1) - 1, n >> 1
        # print(len(a))
        # print(l, r)
        al, ar = l, r
        while al >= 0 and ar < n and a[al] == a[ar]:
            al -= 1
            ar += 1
        bl, br = l, r
        while bl >= 0 and br < n and b[bl] == b[br]:
            bl -= 1
            br += 1
        # print(a[:al + 1], b[ar:][::-1])
        # print(b[:bl + 1], a[br:][::-1])
        return a[:al + 1] == b[ar:][::-1] or b[:bl + 1] == a[br:][::-1] \
               or b[:al + 1] == a[ar:][::-1] or a[:bl + 1] == b[br:][::-1]


def main():
    sol = Solution()
    # a = "ulacfd"
    # b = "jizalu"
    # res = sol.checkPalindromeFormation(a, b)
    # print(res)

    a = "pvhmupgqeltozftlmfjjde"
    b = "yjgpzbezspnnpszebzmhvp"
    res = sol.checkPalindromeFormation(a, b)
    print(res)


if __name__ == '__main__':
    main()
