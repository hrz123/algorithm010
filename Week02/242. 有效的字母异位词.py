# 242. 有效的字母异位词.py


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = [0] * 26  # ascii改为256
        ord_a = ord('a')
        for c in s:
            hashmap[ord(c) - ord_a] += 1

        for c in t:
            tmp = ord(c) - ord_a
            if not hashmap[tmp]:
                return False
            hashmap[tmp] -= 1

        return True


# 使用ascii码
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = [0] * 256

        for c in s:
            hashmap[ord(c)] += 1

        for c in t:
            tmp = ord(c)
            if not hashmap[tmp]:
                return False
            hashmap[tmp] -= 1

        return True


def main():
    s = Solution()
    print(s.isAnagram("anagram", "anagram"))


if __name__ == '__main__':
    main()
