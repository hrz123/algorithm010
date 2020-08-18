# 89. 格雷编码.py
from typing import List


# 设n阶格雷码集合为G(n)，则G(n+1)阶格雷码为：
# 给G(n)阶格雷码每个元素二进制形式前面添加0，得到G'(n)
# 设G(n)集合倒序（镜像）为R(n)，给R(n)每个元素二进制形式前面添加1，得到R'(n)
# G(n+1) = G'(n)∪R'(n)

# 根据以上规律，可从
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res


def main():
    sol = Solution()
    n = 2
    res = sol.grayCode(n)
    print(res)


if __name__ == '__main__':
    main()
