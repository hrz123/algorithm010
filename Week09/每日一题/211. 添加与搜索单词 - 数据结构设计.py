# 211. 添加与搜索单词 - 数据结构设计.py


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_of_word] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)

        def dfs(i, node):
            if i == n:
                if self.end_of_word in node:
                    return True
                return False
            if word[i] != '.':
                if word[i] not in node:
                    return False
                return dfs(i + 1, node[word[i]])
            for c in node:
                if c != self.end_of_word:
                    if dfs(i + 1, node[c]):
                        return True
            return False

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
def main():
    pass


if __name__ == '__main__':
    main()
