# 241. 为运算表达式设计优先级.py
from typing import List


class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        # 如果只有数字，直接返回
        if s.isdigit():
            return [int(s)]
        res = []
        for i, char in enumerate(s):
            if char in {'+', '-', '*'}:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(s[:i])
                right = self.diffWaysToCompute(s[i + 1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
