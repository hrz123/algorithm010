# 733. 图像渲染.py
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        m, n = len(image), len(image[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i, j):
            image[i][j] = newColor
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and image[_i][_j] == color:
                    dfs(_i, _j)

        dfs(sr, sc)
        return image


def main():
    pass


if __name__ == '__main__':
    main()
