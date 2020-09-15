# 336. 回文对.py
from typing import List


# 1.暴力
# 超出时间限制
# 时间复杂度:O(m^2m)其中n是words数组长度，m是元素平均长度
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    if self.isValid(words[i] + words[j]):
                        res.append([i, j])
        return res

    def isValid(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    if self.isValid(words[i], words[j]):
                        res.append([i, j])
        return res

    def isValid(self, s1, s2):
        m, n = len(s1), len(s2)
        k = m if m < n else n
        if m == k:
            return s1[:k] == s2[::-1][:k] and self.isPalindrome(s2[:n - k])
        return s1[:k] == s2[::-1] and self.isPalindrome(s1[k:])

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


# 什么样的两个字符可以构成回文串
# 假设存在两个字符串s1和s2，stack1+s2是一个回文串，记这两个字符串的长度分别为len1和len2，
# 我们可以分三种情况进行讨论
# 1.len1==len2，那么s1是s2的反转
# 2.len(stack1)>len(stack2)，这种情况下我们可以将s1拆成左右两个部分：t1和t2，其中t1是s2的翻转，t2是回文串
# 3.len(stack1)<len(stack2)，这种情况下我们可以将s2拆成左右两个部分：t1和t2，其中t2是s1的翻转，t1是回文串
# 这样，对于每一个字符串，我们令其为s1和s2中较长的那一个，然后找到可能和它构成回文串的字符串即可。
# 具体地说，我们枚举每一个字符串k，令其为s1和s2中较长的那一个，那么k可以被拆分为两部分，t1和t2
# 1.当t1是回文串时，符合情况3，我们只需要查询给定的字符串序列中是否包含t2的翻转
# 2.当t2是回文串时，符合情况2，我们只需要查询给定的字符串序列中是否包含t1的翻转
# 也就是说，我们要枚举字符串k的每一个前缀和后缀，判断其是否为回文串。
# 如果是回文串，我们就查询其剩余部分的翻转是否在给定的字符串序列中出现即可。
# 注意到空串也是回文串，所以我们可以将k拆解为k+∅或∅+k，这样我们就能将情况1也解释为特殊的情况2或情况3.
# 而要实现这些操作，我们只需要设计一个能够在一系列字符串中查询「某个字符串的子串的翻转」是否存在的数据结构，
# 有两种实现方法
# 我们可以使用字典树存储所有的字符串。在进行查询时，我们将待查询的子串逆序地在字典树上进行遍历，
# 即可判断其是否存在
# 我们可以用哈希表存储所有字符串的翻转串。在进行查询时，我们判断待查询串的子串是否在哈希表中出现，
# 就等价于判断了其翻转是否存在。


# The basic idea is to check each word for prefixes (and suffixes)
# that are themselves palindromes.
# If you find a prefix that is a valid palindrome,
# then the suffix reversed can be paired with the word
# in order to make a palindrome. It's better explained with an example.
#
# words = ["bot", "t", "to"]
# Starting with the string "bot". We start checking all prefixes.
# If "", "b", "bo", "bot" are themselves palindromes.
# The empty string and "b" are palindromes.
# We work with the corresponding suffixes ("bot", "ot")
# and check to see if their reverses ("tob", "to")
# are present in our initial word list. If so (like the word to"to"),
# we have found a valid pairing where the reversed suffix can be prepended
# to the current word in order to form "to" + "bot" = "tobot".
#
# You can do the same thing by checking all suffixes
# to see if they are palindromes.
# If so, then finding all reversed prefixes will give you the words
# that can be appended to the current word to form a palindrome.
#
# The process is then repeated for every word in the list.
# Note that when considering suffixes,
# we explicitly leave out the empty string to avoid counting duplicates.
# That is, if a palindrome can be created by appending an entire other word
# to the current word, then we will already consider such a palindrome
# when considering the empty string as prefix for the other word.
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pairs = []
        for word, k in words.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pairs.append([words[back], k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pairs.append([k, words[back]])
        return valid_pairs


class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word, idx):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_of_word] = idx

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return -1
            node = node[c]
        if self.end_of_word in node:
            return node[self.end_of_word]
        return -1


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        trie = Trie()
        for i, w in enumerate(words):
            trie.insert(w, i)

        valid_pairs = []
        for k, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    idx = trie.search(back)
                    if back != word and idx != -1:
                        valid_pairs.append([idx, k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    idx = trie.search(back)
                    if back != word and idx != -1:
                        valid_pairs.append([k, idx])
        return valid_pairs


# 以下为自我练习
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        ret = []
        words = {word: i for i, word in enumerate(words)}
        for word, k in words.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        ret.append([words[back], k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        ret.append([k, words[back]])
        return ret


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        res = []
        words = {w: i for i, w in enumerate(words)}
        for w in words:
            n = len(w)
            for j in range(n + 1):
                pre = w[:j]
                suf = w[j:]
                if is_palindrome(pre):
                    back = suf[::-1]
                    if back != w and back in words:
                        res.append([words[back], words[w]])
                if j != n and is_palindrome(suf):
                    back = pre[::-1]
                    if back != words and back in words:
                        res.append([words[w], words[back]])
        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {w: i for i, w in enumerate(words)}

        def is_palindrome(s):
            return s == s[::-1]

        res = []
        for w in words:
            n = len(w)
            for j in range(n + 1):
                pre = w[:j]
                suf = w[j:]
                if is_palindrome(pre):
                    back = suf[::-1]
                    if back != w and back in words:
                        res.append([words[back], words[w]])
                if j != n and is_palindrome(suf):
                    back = pre[::-1]
                    if back != w and back in words:
                        res.append([words[w], words[back]])
        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {w: i for i, w in enumerate(words)}
        res = []

        def is_palindrome(s):
            return s == s[::-1]

        for w in words:
            n = len(w)
            for i in range(n + 1):
                pre = w[:i]
                suf = w[i:]
                if is_palindrome(pre):
                    back = suf[::-1]
                    if back != w and back in words:
                        res.append([words[back], words[w]])
                if i != n and is_palindrome(suf):
                    back = pre[::-1]
                    if back != w and back in words:
                        res.append([words[w], words[back]])
        return res


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {w: i for i, w in enumerate(words)}

        def is_palindrome(s):
            return s == s[::-1]

        res = []
        for w, i in words.items():
            n = len(w)
            for j in range(n + 1):
                pre = w[:j]
                suf = w[j:]
                if is_palindrome(pre):
                    back = suf[::-1]
                    if back != w and back in words:
                        res.append([words[back], i])
                if j != n and is_palindrome(suf):
                    back = pre[::-1]
                    if back in words:
                        res.append([i, words[back]])
        return res


def main():
    sol = Solution()
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    res = sol.palindromePairs(words)
    print(res)


if __name__ == '__main__':
    main()
