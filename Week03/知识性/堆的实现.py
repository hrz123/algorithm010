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


# 小顶堆
# def minheap(a, i, size):
#     l = 2 * i + 1
#     r = 2 * i + 2
#     small = i
#     if l < size and a[l] < a[small]:
#         small = l
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


def insert(a, data):
    a.append(data)
    i = len(a) - 1
    while i >> 1 >= 0 and a[i >> 1] < a[i]:
        a[i], a[i >> 1] = a[i >> 1], a[i]


def main():
    # 示例
    nums = [3, 2, 5, 1, 4]
    heapsize = len(nums)

    # 建堆
    buildheap(nums, heapsize)
    print(nums)
    # output:
    # [5, 4, 3, 1, 2]

    # 插入
    nums.append(6)
    heapsize += 1
    i = heapsize - 1
    while i >> 1 >= 0 and nums[i] > nums[i >> 1]:
        nums[i], nums[i >> 1] = nums[i >> 1], nums[i]
        i >>= 1
    print(nums)
    # output:
    # [6, 5, 4, 1, 2, 3]

    # 删除
    heapsize -= 1
    nums[0], nums[heapsize] = nums[heapsize], nums[0]
    maxheap(nums, 0, heapsize)
    print(nums)

    # output:
    # [5, 2, 3, 1, 0, 4]


if __name__ == '__main__':
    main()
