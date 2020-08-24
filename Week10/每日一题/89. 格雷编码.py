# 89. 格雷编码.py
from typing import List


# 设n阶格雷码集合为G(n)，则G(n+1)阶格雷码为：
# 给G(n)阶格雷码每个元素二进制形式前面添加0，得到G'(n)
# 设G(n)集合倒序（镜像）为R(n)，给R(n)每个元素二进制形式前面添加1，得到R'(n)
# G(n+1) = G'(n)∪R'(n)

# 根据以上规律，可从0阶格雷码推导出任何阶格雷码
# 代码解析：
# 由于最高位前默认为0，因此G'(n) = G(n)，只需在res(即G(n))添加R'(n)即可
# 计算R'(n):执行head = 1 << i，计算出对应位数，以给R(n)前添加1得到对应R'(n)
# 倒序遍历res（即G(n));一次求得R'(n)各元素添加至res尾端，遍历完成后res即G(n+1)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        head = 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | head)
            head <<= 1
        return res


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [num + (1 << i) for num in reversed(res)]
        return res


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [num + (1 << i) for num in reversed(res)]
        return res


def main():
    sol = Solution()
    n = 2
    res = sol.grayCode(n)
    print(res)
    n = 3
    res = sol.grayCode(n)
    print(res)


if __name__ == '__main__':
    main()
