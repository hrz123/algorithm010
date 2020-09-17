# LCP 19. 秋叶收藏集.py


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        l, r = 0, n - 1
        y_left, y_right = l + 1, r - 1
        r_count_left = 0 if leaves[l] == 'y' else 1
        r_count_right = 0 if leaves[r] == 'y' else 1
        res = n
        y_count = leaves[1:-1].count('y')
        while y_left <= y_right:
            if r_count_left >= (y_left // 2) and r_count_right >= (
                    (r - y_right) // 2):
                while y_left <= y_right and leaves[y_left] == 'r':
                    r_count_left += 1
                    y_left += 1
                while y_left <= y_right and leaves[y_right] == 'r':
                    r_count_right += 1
                    y_right -= 1
                tmp = n - y_count - r_count_left - r_count_right
                if y_count == 0:
                    tmp += 1
                res = min(res, tmp)
                y_count -= 1
                y_left += 1
            elif r_count_left < (y_left // 2):
                if leaves[y_left] == 'r':
                    r_count_left += 1
                else:
                    y_count -= 1
                y_left += 1
            else:
                if leaves[y_right] == 'r':
                    r_count_right += 1
                else:
                    y_count -= 1
                y_right -= 1

        return res


# class Solution:
#     def minimumOperations(self, leaves: str) -> int:
#         n = len(leaves)
#         l, r = 0, n - 1
#         y_left, y_right = l + 1, r - 1
#         r_count_left = 0 if leaves[l] == 'y' else 1
#         r_count_right = 0 if leaves[r] == 'y' else 1
#         res = n
#         y_count = leaves[1:-1].count('y')
#         import sys
#         sys.setrecursionlimit(10 ** 9)
#
#         def helper(y_left, y_right, y_count):
#             nonlocal r_count_left, r_count_right, res
#             while y_left <= y_right:
#                 if r_count_left > (y_left // 2) or r_count_right > (
#                         (r - y_right) // 2) or y_count > (
#                         y_right - y_left + 1) // 2:
#                     while y_left <= y_right and leaves[y_left] == 'r':
#                         r_count_left += 1
#                         y_left += 1
#                     while y_left <= y_right and leaves[y_right] == 'r':
#                         r_count_right += 1
#                         y_right -= 1
#                     tmp = n - y_count - r_count_left - r_count_right
#                     if y_count == 0:
#                         tmp += 1
#                     res = min(res, tmp)
#                     res = min(res, helper(y_left + 1, y_right, y_count - 1),
#                               helper(y_left, y_right - 1, y_count - 1))
#                     return res
#                 elif r_count_left <= (y_left // 2):
#                     if leaves[y_left] == 'r':
#                         r_count_left += 1
#                     else:
#                         y_count -= 1
#                     y_left += 1
#                 else:
#                     if leaves[y_right] == 'r':
#                         r_count_right += 1
#                     else:
#                         y_count -= 1
#                     y_right -= 1
#             return res
#
#         return helper(y_left, y_right, y_count)


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        a = 0
        b = c = float('inf')
        for leave in leaves:
            x = int(leave == 'y')
            a, b, c = a + x, min(a, b) + (1 - x), min(b, c) + x
        return c


def main():
    sol = Solution()

    leaves = "rryyrrrryrrryyyyyrr"
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "ry" * 100000
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "ry" * 4
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "rrryyyrryyyrr"
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "ryr"
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "yyy"
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "ryr" * 3
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "r" * 100000
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "ryyyr"
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "yrrrrry"
    res = sol.minimumOperations(leaves)
    print(res)

    leaves = "y" * 100000
    res = sol.minimumOperations(leaves)
    print(res)


if __name__ == '__main__':
    main()
