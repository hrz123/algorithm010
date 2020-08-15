# 树状数组binary-indexed-tree.py


class BITree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)
        for i, num in enumerate(nums):
            self.update(i + 1, num)

    def update(self, i, k):
        """

        Args:
            i: 指的是更新数组中的第几个数，对应索引是i-1
            k: 更新的数值

        """
        while i <= self.n:
            self.tree[i] += k
            i += (i & -i)

    def getSum(self, i):
        """

        Args:
            i: 返回前几个数的前缀和

        Returns: 前i个数的前缀和

        """
        s = 0
        while i:
            s += self.tree[i]
            i -= (i & -i)
        return s


def update(i, n, k=1):
    while i <= n:
        BITree[i] += k
        i += i & -i


def getSum(i):
    s = 0
    while i:
        s += BITree[i]
        i -= i & -i
    return s


def main():
    nums = [1, 2, 3, 4]
    tree = BITree(nums)
    # 打印前1,2,3,4个数的前缀和
    print(tree.getSum(1))
    print(tree.getSum(2))
    print(tree.getSum(3))
    print(tree.getSum(4))
    # 更新第2个数的值，增加3
    tree.update(2, 3)
    # 再次打印前1,2,3,4个数的前缀和
    print(tree.getSum(1))
    print(tree.getSum(2))
    print(tree.getSum(3))
    print(tree.getSum(4))
    # 更新第2个数的值，减少3
    tree.update(2, -3)
    print(tree.getSum(1))
    print(tree.getSum(2))
    print(tree.getSum(3))
    print(tree.getSum(4))


if __name__ == '__main__':
    main()
