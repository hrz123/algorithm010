# 168.Excel表列名称.py


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""

        while n:
            n -= 1
            n, mod = divmod(n, 26)
            res = chr(mod + 65) + res

        return res


# class Solution:
#     def convertToTitle(self, m: int) -> str:
#         if m == 0:
#             return ""
#         div, mod = divmod(m - 1, 26)
#         return self.convertToTitle(div) + chr(mod + 65)


# class Solution:
#     def convertToTitle(self, m: int) -> str:
#         return "" if m == 0 else self.convertToTitle((m - 1) // 26) + chr(
#             (m - 1) % 26 + 65)


# 以下为自我练习
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n -= 1
            n, mod = divmod(n, 26)
            res = chr(65 + mod) + res
        return res


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        a_upper = ord('A')
        while n:
            n, mod = divmod(n - 1, 26)
            res = chr(a_upper + mod) + res
        return res


def main():
    s = Solution()
    res = s.convertToTitle(28)
    print(res)


if __name__ == '__main__':
    main()
