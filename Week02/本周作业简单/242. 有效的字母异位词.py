# 242. 有效的字母异位词.py

# 1.最简单的方法：两个字符串按ascii吗值的大小排序，比较字符串相等
# 时间复杂度：排序：O(NlogN)，比较O(N)，总体O(NlogN)
# 空间复杂度：O(1)
# 2.用一个hashmap记录字符串出现的字符和次数，再遍历另一个字符串依次减一。
# 保证字符创长度相等的情况下，不出现负数即为相等。
# 时间复杂度：遍历两个字符串O(N)
# 空间复杂度：cache O(N)
# 3.如果字符串中的字符有界。比如只有英文小写字母，ascii吗（0-255）。
# 那么记录字符与出现次数的hashmap也可替换为数组（桶排序的思想）。其他与前面方法一致。
# 时间复杂度：O(N)同上
# 空间复杂度：O(N)。替换hashmap的数组


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
