# 堆的实现.py


# 大顶堆
def maxheap(a, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    large = i
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[i], a[large] = a[large], a[i]
        maxheap(a, large, size)


def buildheap(a, size):
    for i in range(size >> 1, -1, -1):
        maxheap(a, i, size)


def insert(a, val, size):
    a.append(val)
    assert a[size - 1] == val
    i = size - 1
    p = i >> 1
    while p >= 0 and a[p] < a[i]:
        a[p], a[i] = a[i], a[p]
        i = p
        p = i >> 1


def max_heap(a, i, size):
    l = i * 2 + 1
    r = i * 2 + 2
    large = i
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[large], a[i] = a[i], a[large]
        max_heap(a, large, size)


def build_heap(a, size):
    for i in range(size >> 1, -1, -1):
        max_heap(a, i, size)


def insert(a, val, size):
    i = size
    size += 1
    p = i >> 1
    while p >= 0 and a[p] < a[i]:
        a[p], a[i] = a[i], a[p]
        i = p
        p = i >> 1


# 小顶堆
# def minheap(a, i, size):
#     m = 2 * i + 1
#     r = 2 * i + 2
#     small = i
#     if m < size and a[m] < a[small]:
#         small = m
#     if r < size and a[r] < a[small]:
#         small = r
#     if small != i:
#         a[i], a[small] = a[small], a[i]
#         minheap(a, small, size)
#
#
# def buildheap(a, size):
#     for i in range(size >> 1, -1, -1):
#         minheap(a, i, size)


# 以下为自我练习
def maxheap(a, i, size):
    l = i * 2 + 1
    r = i * 2 + 1
    large = i
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[i], a[large] = a[large], a[i]
        maxheap(a, large, size)


def buildheap(a, size):
    for i in range(size >> 1, -1, -1):
        maxheap(a, i, size)


def max_heap(a, i, size):
    l = i * 2 + 1
    r = i * 2 + 2
    large = i
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[large], a[i] = a[i], a[large]
        max_heap(a, large, size)


def build_heap(a, size):
    for i in range(size >> 1, -1, -1):
        max_heap(a, i, size)


#
#
# def insert(a, val):
#     a.append(val)
#     i = len(a) - 1
#     p = i >> 1
#     while a[p] < a[i]:
#         a[p], a[i] = a[i], a[p]
#         i = p
#         p = i >> 1


def max_heap(a, i, size):
    l = i * 2 + 1
    r = i * 2 + 2
    large = i
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[large], a[i] = a[i], a[large]
        max_heap(a, large, size)


def build_heap(a, size):
    for i in range(size >> 1, -1, -1):
        max_heap(a, i, size)


def max_heap(a, i, size):
    l = i * 2 + 1
    r = i * 2 + 2
    large = i
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[i], a[large] = a[large], a[i]
        max_heap(a, large, size)


def build_heap(a, size):
    for i in range(size >> 1, -1, -1):
        max_heap(a, i, size)


def max_heap(a, i, size):
    large = i
    l = i * 2 + 1
    r = i * 2 + 2
    if l < size and a[l] > a[large]:
        large = l
    if r < size and a[r] > a[large]:
        large = r
    if large != i:
        a[large], a[i] = a[i], a[large]
        max_heap(a, large, size)


def build_heap(a, size):
    for i in range(size >> 1, -1, -1):
        max_heap(a, i, size)


def main():
    def maxheap(a, i, size):
        l = 2 * i + 1
        r = 2 * i + 2
        large = i
        if l < size and a[l] > a[large]:
            large = l
        if r < size and a[r] > a[large]:
            large = r
        if large != i:
            a[i], a[large] = a[large], a[i]
            maxheap(a, large, size)

    def buildheap(a, size):
        for i in range(size >> 1, -1, -1):
            maxheap(a, i, size)

    # 示例
    nums = [3, 2, 5, 1, 4]
    heapsize = len(nums)

    # 建堆
    buildheap(nums, heapsize)
    print(nums)
    # output:
    # [5, 4, 3, 1, 2]

    # 插入
    # nums.append(6)
    # heapsize += 1
    # i = heapsize - 1
    # while i >> 1 >= 0 and nums[i] > nums[i >> 1]:
    #     nums[i], nums[i >> 1] = nums[i >> 1], nums[i]
    #     i >>= 1
    # print(nums)
    # heapsize += 1
    # insert(nums, 6, heapsize)
    # print(nums)
    # output:
    # [6, 5, 4, 1, 2, 3]

    # 删除
    # heapsize -= 1
    # nums[0], nums[heapsize] = nums[heapsize], nums[0]
    # maxheap(nums, 0, heapsize)
    # print(nums)

    # output:
    # [5, 2, 3, 1, 0, 4]


if __name__ == '__main__':
    main()
