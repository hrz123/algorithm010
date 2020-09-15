# 68. 文本左右对齐.py
from typing import List


class Solution:

    def process(self, curLen, curWords, maxWidth):
        # 空格数量
        num_space = maxWidth - curLen
        # 如果只有一个单词就没必要考虑分配，直接填充空格即可
        if len(curWords) == 1:
            return curWords[0] + ' ' * (maxWidth - curLen)
        # 每个空隙分到的空格数量
        num_sep = num_space // (len(curWords) - 1)
        # 分到空格数量多一个的空隙
        head_sep = num_space % (len(curWords) - 1)
        cur = ''
        # 分配
        for i in range(len(curWords) - 1):
            cur = cur + curWords[i] + (
                ' ' * (num_sep + 1) if i < head_sep else ' ' * num_sep)
        # 分配结束之后把最后一个单词连上
        cur = cur + curWords[-1]
        return cur

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        curLen, curWords = 0, []

        for w in words:
            # 切分判断的条件，单词长度加上基本的空格长度
            if curLen + len(w) + len(curWords) <= maxWidth:
                curLen += len(w)
                curWords.append(w)
            else:
                ret.append(self.process(curLen, curWords, maxWidth))
                curLen, curWords = len(w), [w]

        # 剩下没有安排的就是最后一行，按照最后一行靠左处理
        if len(curWords) > 0:
            cur = ''
            for i in range(len(curWords) - 1):
                cur = cur + curWords[i] + ' '
            cur = cur + curWords[-1]
            cur += ' ' * (maxWidth - len(cur))
            ret.append(cur)
        return ret


def main():
    pass


if __name__ == '__main__':
    main()
