# 58. 最后一个单词的长度.py


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        res = 0
        while j >= 0 and s[j] == ' ':
            j -= 1
        while j >= 0 and s[j] != ' ':
            j -= 1
            res += 1
        return res


# 以下为自我练习
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        res = 0
        while j >= 0 and s[j].isalnum():
            res += 1
            j -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
