# 13. 罗马数字转整数.py


class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
            "I":  1,
            "V":  5,
            "X":  10,
            "L":  50,
            "C":  100,
            "D":  500,
            "M":  1000

        }
        ans = 0
        i = 0
        while i < len(s):
            if s[i] in 'IXC' and i + 1 < len(s) and s[i:i + 2] in hashmap:
                ans += hashmap[s[i:i + 2]]
                i += 2
            else:
                ans += hashmap[s[i]]
                i += 1
        return ans


def main():
    sol = Solution()
    s = "MCMXCIV"
    res = sol.romanToInt(s)
    print(res)


if __name__ == '__main__':
    main()
