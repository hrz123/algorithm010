# 5519. 重新排列单词间的空格.py
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = text.count(' ')
        if len(words) == 1:
            return words[0] + ' ' * spaces
        div, mod = divmod(spaces, len(words) - 1)
        s = ' ' * div
        tmp = s.join(words)
        return tmp + ' ' * mod


def main():
    sol = Solution()
    s = "  this   is  a sentence "
    res = sol.reorderSpaces(s)
    print(res)


if __name__ == '__main__':
    main()
