# LRU-cache-python示例使用OrderedDictAPI实现.py
import collections


# 使用 OrderedDict 容器就很简单
class LRUCache(object):
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v  # key as the newest one
        return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)
        self.dic[key] = value


def main():
    pass


if __name__ == '__main__':
    main()
