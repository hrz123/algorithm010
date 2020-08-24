# 1255. 得分最高的单词集合.py
from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str],
                      score: List[int]) -> int:
        def dfs(i, cur_letters):
            if i == n:
                return 0
            res = dfs(i + 1, cur_letters)
            ith_letter = Counter(words[i])
            check = all(cur_letters[k] >= v for k, v in ith_letter.items())
            if check:
                ith_score = sum(
                    score[ord(k) - 97] * v for k, v in ith_letter.items())
                cur_letters -= ith_letter
                res = max(res, ith_score + dfs(i + 1, cur_letters))
                cur_letters += ith_letter
            return res

        n = len(words)
        c_letters = Counter(letters)
        return dfs(0, c_letters)


def main():
    pass


if __name__ == '__main__':
    main()
