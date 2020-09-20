# 5506. 奇怪的打印机 II.py
import collections
from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors = collections.defaultdict(set)  # 【同种颜色格子坐标集合】
        for r, row in enumerate(targetGrid):
            for c, pt in enumerate(row):
                colors[pt].add((r, c))

        scale = {p: [
            min(r for r, c in colors[p]),
            min(c for r, c in colors[p]),
            max(r for r, c in colors[p]),
            max(c for r, c in colors[p])]
            for p in colors
        }  # 【覆盖某颜色所需的最小矩形】

        unfilled = {p: set(
            (r, c)
            for r in range(scale[p][0], scale[p][2] + 1)
            for c in range(scale[p][1], scale[p][3] + 1)
            if targetGrid[r][c] != p
        )
            for p in colors
        }  # 【某颜色的最小矩形中，不是该颜色的格子坐标集合】

        while unfilled:
            for p in unfilled:
                if not unfilled[p]:  # 选取一个可以上色的颜色；
                    break
            else:
                return False  # 如果没有，则说明没有合适的方案，返回false；
            unfilled.pop(p)
            for q in unfilled:
                unfilled[q] -= colors[p]  # 上色的过程，去掉其他所有元素的unfilled
        return True


def main():
    pass


if __name__ == '__main__':
    main()
