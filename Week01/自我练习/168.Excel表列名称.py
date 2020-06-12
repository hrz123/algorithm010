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
#     def convertToTitle(self, n: int) -> str:
#         if n == 0:
#             return ""
#         div, mod = divmod(n - 1, 26)
#         return self.convertToTitle(div) + chr(mod + 65)


# class Solution:
#     def convertToTitle(self, n: int) -> str:
#         return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr(
#             (n - 1) % 26 + 65)


def main():
    s = Solution()
    res = s.convertToTitle(1)
    print(res)


if __name__ == '__main__':
    main()
