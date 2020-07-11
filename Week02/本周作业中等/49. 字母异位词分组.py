# 49. 字母异位词分组.py
import collections
from typing import List


# 1.建里一个sorted（str）：List[str]的hashmap。输出hashmap所有的value即可。
# 做法比较，这里不赘述。
# 时间复杂度：O(NKlogK)，其中 N 是 strs 的长度，而 K 是 strs
# 中字符串的最大长度。当我们遍历每个字符串时，外部循环具有的复杂度为 O(N)。
# 然后，我们在 O(KlogK) 的时间内对每个字符串排序。
# 空间复杂度：O(NK)，排序存储在 ans 中的全部信息内容。
# 2.因为字符是有界的。sorted可以使用计数排序。O(N)的排序算法。
# 时间复杂度：O(NK)，其中 N 是 strs 的长度，
# 而 K 是 strs 中字符串的最大长度。
# 计算每个字符串的字符串大小是线性的，我们统计每个字符串。
# 空间复杂度：O(NK)，排序存储在 ans 中的全部信息内容。


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sorted_s = self.bucket_sort(s)
            if sorted_s in hashmap:
                hashmap[sorted_s].append(s)
            else:
                hashmap[sorted_s] = [s]

        return list(hashmap.values())

    def bucket_sort(self, string: str) -> str:
        arr = [0] * 26
        li = []
        for c in string:
            arr[ord(c) - ord('a')] += 1
        for i, e in enumerate(arr):
            li.append(chr(ord('a') + i) * e)

        return ''.join(li)


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


# 以下为自我练习
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = set()
        # 可以使用
        res = []

        for s in strs:
            if s not in hashmap:
                hashmap.add(sorted(s))
                res.append()


def main():
    pass


if __name__ == '__main__':
    main()
c