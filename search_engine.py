# search_engine.py
import re
from collections import defaultdict


class SearchEngine(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented')


class SimpleEngine(SearchEngine):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


class BOWEngine(SearchEngine):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        # remove punctuations and \n
        text = re.sub(r'[^\w]', ' ', text)
        # to lower
        text = text.lower()
        # generate all words list
        word_list = text.split(' ')
        # remove space
        word_list = filter(None, word_list)
        # return set of words
        return set(word_list)


#
#
class BOWInvertedIndexEngine(SearchEngine):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = defaultdict(list)

    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)
        for word in words:
            self.inverted_index[word].append(id)

    def search(self, query):
        query_words = [*self.parse_text_to_words(query)]
        query_words_index = [0] * len(query_words)

        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        result = []
        while True:
            current_ids = []
            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                if current_index >= len(current_inverted_list):
                    return result
                current_ids.append(current_inverted_list[current_index])
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x + 1 for x in query_words_index]
                continue
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_pos] += 1

    @staticmethod
    def parse_text_to_words(text):
        # remove punctuations and \n
        text = re.sub(r'[^\w]', ' ', text)
        # to lower
        text = text.lower()
        # generate all words list
        word_list = text.split(' ')
        # remove space
        word_list = filter(None, word_list)
        # return set of words
        return set(word_list)


class DLinkedNode(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, k=32):
        self.cap = k
        self.size = 0
        self.mem = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.mem:
            node = self.mem[key]
            self.moveToHead(node)
            return node.val
        return -1

    def put(self, key, val):
        if key in self.mem:
            node = self.mem[key]
            node.val = val
            self.moveToHead(node)
        else:
            if self.size == self.cap:
                node = self.removeTail()
                self.mem.pop(node.key)
                self.size -= 1
            node = DLinkedNode(key, val)
            self.addToHead(node)
            self.mem[key] = node
            self.size += 1

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)

    def search(self, query):
        if self.get(query) != -1:
            print('cache hit!')
            return self.get(query)
        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.put(query, result)
        return result


def main(search_engine):
    for file_path in ('1.txt', '2.txt', '3.txt', '4.txt', '5.txt'):
        search_engine.add_corpus(file_path)
    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


if __name__ == '__main__':
    # search_engine = SimpleEngine()
    # search_engine = BOWEngine()
    # search_engine = BOWInvertedIndexEngine()
    search_engine = BOWInvertedIndexEngineWithCache()
    main(search_engine)
