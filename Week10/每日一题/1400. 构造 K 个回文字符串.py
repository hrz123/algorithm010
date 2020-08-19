# 1400. 构造 K 个回文字符串.py
import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # 右边界为字符串的长度
        right = len(s)
        # 统计每个字符出现的次数
        occ = collections.Counter(s)
        # 左边界为出现奇数次字符的个数
        left = sum(1 for _, v in occ.items() if v % 2 == 1)
        # 注意没有出现奇数次的字符的特殊情况
        left = max(left, 1)
        return left <= k <= right


def main():
    pass


if __name__ == '__main__':
    main()
