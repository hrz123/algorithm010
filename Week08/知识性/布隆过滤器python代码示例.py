# 布隆过滤器python代码示例.py
import mmh3
from bitarray import bitarray


class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if self.bit_array[result] == 0:
                return "Nope"
        return "Probably"


# 以下为自我练习
class BloomFilter:
    def __init__(self, size: int, hash_num: int):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, s):
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if not self.bit_array[result]:
                return "Nope"
        return "Probably"


class BloomFilter:
    def __init__(self, size: int, hash_num: int):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s: str) -> None:
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            self.bit_array[result] = 1

    def search(self, s: str) -> bool:
        for seed in range(self.hash_num):
            result = mmh3.hash(s, seed) % self.size
            if not self.bit_array[result]:
                return False
                # Nope
        return True
        # Probably


class BloomFilter:
    def __init__(self, size: int, hash_num: int):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s: str):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            self.bit_array[res] = 1

    def search(self, s: str):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            if not self.bit_array[res]:
                return False
        return True


class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            self.bit_array[res] = 1

    def search(self, s):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            if not self.bit_array[res]:
                return False
        return True


class BloomFilter:
    def __init__(self, size: int, hash_num: int):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            self.bit_array[res] = 1

    def search(self, s):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            if not self.bit_array[res]:
                return False
        return True


class BloomFilter:
    def __init__(self, size, hash_num):
        self.size = size
        self.hash_num = hash_num
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, s):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            self.bit_array[res] = 1

    def search(self, s):
        for seed in range(self.hash_num):
            res = mmh3.hash(s, seed) % self.size
            if not self.bit_array[res]:
                return False
        return True


def main():
    bf = BloomFilter(500000, 7)
    bf.add("dantezhao")
    print(bf.search("dantezhao"))
    print(bf.search("yyj"))


if __name__ == '__main__':
    main()
