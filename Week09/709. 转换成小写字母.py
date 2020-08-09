# 709. 转换成小写字母.py


class Solution:
    def toLowerCase(self, s: str) -> str:
        tmp = list(s)
        for i in range(len(s)):
            if 65 <= ord(tmp[i]) <= 90:
                tmp[i] = chr(ord(tmp[i]) + 32)
        return ''.join(tmp)


# 以下为自我练习
class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                s[i] = chr(ord(s[i]) + 32)
        return ''.join(s)


def main():
    pass


if __name__ == '__main__':
    main()
