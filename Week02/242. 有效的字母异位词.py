# 242. 有效的字母异位词.py


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        memo = [0] * 26  # ascii改为256
        ord_a = ord('a')
        for c in s:
            memo[ord(c) - ord_a] += 1

        for c in t:
            tmp = ord(c) - ord_a
            if not memo[tmp]:
                return False
            memo[tmp] -= 1

        return True


def main():
    s = Solution()
    print(s.isAnagram("anagram", "anagram"))


if __name__ == '__main__':
    main()
