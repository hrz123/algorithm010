# 151. 翻转字符串里的单词.py


class Solution:
    def reverseWords(self, s: str) -> str:
        cur_word = ''
        word_list = []
        for c in s:
            if c != " ":
                cur_word += c
            else:
                if cur_word:
                    word_list.append(cur_word)
                    cur_word = ""
        if cur_word:
            word_list.append(cur_word)
        return ' '.join(reversed(word_list))


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []
        cur_word = ''

        for c in s:
            if c == ' ':
                if cur_word:
                    word_list.append(cur_word)
                    cur_word = ''
                continue
            cur_word += c
        if cur_word:
            word_list.append(cur_word)
        return ' '.join(reversed(word_list))


def main():
    s = "the sky is blue"
    sol = Solution()
    res = sol.reverseWords(s)
    print(res)


if __name__ == '__main__':
    main()
