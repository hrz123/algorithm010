# 面试题 16.18. 模式匹配.py
import re


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        cnt_a, cnt_b, n = 0, 0, len(value)  # 计算a和b的个数，n为value长度
        for ch in pattern:
            if ch == 'a':
                cnt_a += 1
            else:
                cnt_b += 1

        if n == 0:  # 判断各种边界情况，pattern或者value为空
            return not cnt_a & cnt_b
        else:
            if cnt_a == 0 and cnt_b == 0:
                return False
            elif cnt_a == 0 or cnt_b == 0:  # 判断pattern全是a或者全是b的情况
                if cnt_a == 0:
                    cnt_a, cnt_b = cnt_b, cnt_a  # 如果cnta为0，两者调换一下
                if n % cnt_a != 0:  # 不能整除的情况
                    return False
                d, judge = n // cnt_a, set()  # 用集合来判断是否有第二种字符串出现
                for i in range(cnt_a):
                    judge.add(value[i * d:i * d + d - 1])
                    if len(judge) > 1:
                        break
                return len(judge) == 1  # 如果自始至终只有一种字符串，那么就是True

        for i in range(0, n // cnt_a + 1):  # 一般情况
            if (n - i * cnt_a) % cnt_b == 0:  # 只判断能整除的情况
                j = (n - i * cnt_a) // cnt_b
                cur, judge = 0, set()
                for ch in pattern:  # 用集合来判断是否有第三种字符串出现
                    if ch == 'a':
                        judge.add(value[cur:cur + i])
                        cur += i
                    else:
                        judge.add(value[cur:cur + j])
                        cur += j
                    if len(judge) > 2:
                        break
                if len(judge) == 2:
                    return True  # 如果自始至终只有两种字符串，那么就是True
        return False


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        # 边界情况处理
        if not pattern:
            return not value
        if len(pattern) == 1:
            return True

        # 构造正则表达式：重点是正则表达式的“后向引用”
        reg_a, reg_b = ('\\1', '\\2') if pattern[0] == 'a' else ('\\2', '\\1')
        p = pattern.replace('a', '(\\w*)', 1).replace('b', '(\\w*)', 1).replace(
            'a', reg_a).replace('b', reg_b)
        p = '^' + p + '$'
        m = re.match(p, value)

        # 匹配到 && (模式长度为1 || 模式长度为2 && 两个模式不相同)
        return bool(
            m and (len(m.groups()) == 1 or m.groups()[0] != m.groups()[1]))


# 官方题解
# https://leetcode-cn.com/problems/pattern-matching-lcci/solution/mo-shi-pi-pei-by-leetcode-solution/
# 比较好
# class Solution:
#     def patternMatching(self, pattern: str, value: str) -> bool:
#         count_a = sum(1 for ch in pattern if ch == 'a')
#         count_b = len(pattern) - count_a
#         if count_a < count_b:
#             count_a, count_b = count_b, count_a
#             pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
#
#         if not value:
#             return count_b == 0
#         if not pattern:
#             return False
#
#         for len_a in range(len(value) // count_a + 1):
#             rest = len(value) - count_a * len_a
#             if (count_b == 0 and rest == 0) or (
#                     count_b != 0 and rest % count_b == 0):
#                 len_b = 0 if count_b == 0 else rest // count_b
#                 pos, correct = 0, True
#                 value_a, value_b = None, None
#                 for ch in pattern:
#                     if ch == 'a':
#                         sub = value[pos:pos + len_a]
#                         if not value_a:
#                             value_a = sub
#                         elif value_a != sub:
#                             correct = False
#                             break
#                         pos += len_a
#                     else:
#                         sub = value[pos:pos + len_b]
#                         if not value_b:
#                             value_b = sub
#                         elif value_b != sub:
#                             correct = False
#                             break
#                         pos += len_b
#                 if correct and value_a != value_b:
#                     return True
#
#         return False


# 以下为自我练习
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        if not value:
            return not count_b
        if not pattern:
            return False

        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and not rest %
                                                                     count_b):
                len_b = rest // count_b if count_b else 0
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

        if not value:
            return count_b == 0
        if not pattern:
            return False

        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (
                    count_b != 0 and not rest % count_b):
                len_b = rest // count_b if count_b else 0
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = pattern.count('a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if c == 'b' else 'b' for c in pattern)
        if not value:
            return count_b == 0
        if not pattern:
            return False
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - len_a * count_a
            if (count_b == 0 and rest == 0) \
                    or (count_b != 0 and not rest % count_b):
                len_b = rest // count_b if count_b else 0
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = pattern.count('a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if c == 'b' else 'b' for c in pattern)
        if not value:
            return count_b == 0
        if not pattern:
            return False
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - len_a * count_a
            if (count_b == 0 and rest == 0) \
                    or (count_b != 0 and not rest % count_b):
                len_b = rest // count_b if count_b else 0
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif sub != value_a:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif sub != value_b:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = pattern.count('a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if c == 'b' else 'b' for c in pattern)
        if not value:
            return count_b == 0
        if not pattern:
            return False
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - len_a * count_a
            if (count_b == 0 and rest == 0) or (count_b and not rest % count_b):
                len_b = rest // count_b if count_b else 0
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        else:
                            if sub != value_a:
                                correct = False
                                break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        else:
                            if sub != value_b:
                                correct = False
                                break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = pattern.count('a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if c == 'b' else 'b' for c in pattern)
        if not value:
            return count_b == 0
        if not pattern:
            return False
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest %
                                                count_b == 0):
                len_b = rest // count_b if count_b != 0 else 0
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos + len_a]
                        if not value_a:
                            value_a = sub
                        else:
                            if value_a != sub:
                                correct = False
                                break
                        pos += len_a
                    else:
                        sub = value[pos:pos + len_b]
                        if not value_b:
                            value_b = sub
                        else:
                            if value_b != sub:
                                correct = False
                                break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        return False


def main():
    sol = Solution()

    pattern = "abba"
    value = "dogcatcatdog"
    res = sol.patternMatching(pattern, value)
    print(res)

    pattern = "a"
    value = ""
    res = sol.patternMatching(pattern, value)
    print(res)

    pattern = "bbbaa"
    value = "xxxxxxy"
    res = sol.patternMatching(pattern, value)
    print(res)


if __name__ == '__main__':
    main()
