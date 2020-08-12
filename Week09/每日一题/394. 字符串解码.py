# 394. 字符串解码.py


# 1.栈
# 本题难点在于括号内嵌套库昊，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。
# 算法流程：
# 1.构建辅助栈stack，遍历字符串s中的每一个字符c；
# 当c为数字时，将数字字符转化为数字multi，用于后续倍数计算
# 当c为字母时，在res尾部添加c；
# 当c为'['时，将当前multi和res入栈，并分别置空0：
#    记录此'['前的临时结果res至栈，用于发现对应]后的拼接操作
#    记录此'['前的倍数multi至栈，用于发现对应]后，获取multi * [...]字符串。
# 当c为']'时，stack出栈，拼接字符串res = last_res +cur_multi * res，其中：
# last_res是上个[到当前[的字符串，例如"3[a2[c]]"中的a;
# cur_multi是当前[到]字符串的重复倍数，例如"3[a2[c]]"中的2。
# 返回字符串res
# 时间复杂度O(N)，一次遍历s
# 空间复杂度O(N)，辅助栈在极端情况下需要线性空间，例如2[2[2[a]]]。
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


# 2.递归法
# 总体思路与辅助栈法一直，不同点在于将[和]分别作为递归的开启和终止条件：
# 当s[i] == ']'时，返回当前括号内记录的res字符串与]的索引i（更新上层递归指针位置）
# 当s[i] == '['时，开启新一层递归，记录此[...]内字符串tmp和递归后的最新索引i，
# 并执行res + multi * tmp拼接字符串
# 复杂度分析O(N)，递归会更新索引，因此实际上还是一次遍历s
# 空间复杂度O(N)，极端情况下递归深度将会达到线性级别.
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)


# 以下为自我练习
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append([multi, res])
                res = ""
                multi = 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += c
        return res


class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multi = 0
        res = ""
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append((multi, res))
                multi = 0
                res = ""
            elif c == ']':
                pre_multi, pre_res = stack.pop()
                res = pre_res + pre_multi * res
            else:
                res += c
        return res


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multi = 0
        res = ""
        for c in s:
            if c.isdigit():
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append((multi, res))
                multi = 0
                res = ""
            elif c == ']':
                pre_multi, pre_res = stack.pop()
                res = pre_res + pre_multi * res
            else:
                res += c
        return res


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multi = 0
        res = ""
        for c in s:
            if c.isdigit():
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append((multi, res))
                multi = 0
                res = ""
            elif c == ']':
                pre_multi, pre_res = stack.pop()
                res = pre_res + pre_multi * res
            else:
                res += c
        return res


def main():
    sol = Solution()

    s = "3[a]2[bc]"
    res = sol.decodeString(s)
    print(res)

    s = "3[a2[c]]"
    res = sol.decodeString(s)
    print(res)


if __name__ == '__main__':
    main()
