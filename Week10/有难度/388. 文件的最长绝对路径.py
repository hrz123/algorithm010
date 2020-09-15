# 388. 文件的最长绝对路径.py


# 因为后面的文件只与前面最深的文件有关，只需记录在每个缩进个数的长度即可
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if "." not in input:
            return 0
        depth_dict = {0: 0}
        max_depth = 0
        for line in input.split("\n"):
            # print(line)
            name = line.lstrip("\t")
            depth = len(line) - len(name)
            if "." in name:
                max_depth = max(max_depth, len(name) + depth_dict[depth])
            else:
                depth_dict[depth + 1] = len(name) + depth_dict[depth] + 1
        # print(depth_dict)
        return max_depth


# 我们可以通过 \t的个数看这个文件夹(文件)缩进多少?
# class Solution:
#     def lengthLongestPath(self, input: str) -> int:
#
#         def cal_len(stack):
#             ans = 0
#             for s in stack:
#                 ans += len(s[1])
#             # 多加 len(stack) - 1 个 "/"
#             return ans + len(stack) - 1
#
#         s = input.split("\m")
#         # 记录缩进个数和字符串
#         t = []
#         for a in s:
#             num = a.count("\t")
#             t.append([num, a[num:]])
#         stack = []
#         res = 0
#         for a in t:
#             # 总是保证栈顶是小于该文件的缩进的
#             while stack and stack[-1][0] >= a[0]:
#                 stack.pop()
#             stack.append(a)
#             if "." in a[1]:
#                 # print(stack)
#                 res = max(res, cal_len(stack))
#
#         return res


def main():
    sol = Solution()
    s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t" \
        "\tsubsubdir2\n\t\t\tfile2.ext"
    res = sol.lengthLongestPath(s)
    print(res)
    assert res == 32


if __name__ == '__main__':
    main()
