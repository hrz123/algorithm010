# 874. 模拟行走机器人.py
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  # r
                di = (di - 1) % 4
            elif cmd == -1:  # r
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x * x + y * y)

        return ans


# 以下为自我练习
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = 0
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        direction = 0
        res = 0
        # 好用
        obstacles = set(map(tuple, obstacles))

        for c in commands:
            if c > 0:
                for step in range(c):
                    if (x + dx[direction], y + dy[direction]) in \
                            obstacles:
                        break
                    x += dx[direction]
                    y += dy[direction]
                    res = max(res, x * x + y * y)
            elif c == -1:
                direction = (direction + 1) % 4
            elif c == -2:
                direction = (direction - 1) % 4

        return res


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        x, y, direction, res = 0, 0, 0, 0
        dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
        for c in commands:
            if c == -1:
                direction = (direction + 1) & 3
            elif c == -2:
                direction = (direction - 1) & 3
            else:
                for _ in range(c):
                    if (x + dx[direction], y + dy[direction]) in obstacles:
                        break
                    x += dx[direction]
                    y += dy[direction]
                    res = max(res, x * x + y * y)
        return res


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        obstacles = set(map(tuple, obstacles))
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        k = 0
        x, y = 0, 0
        for c in commands:
            if c == -1:
                k = (k + 1) & 0b11
            elif c == -2:
                k = (k - 1) & 0b11
            else:
                for i in range(c):
                    if (x + dirs[k][0], y + dirs[k][1]) in obstacles:
                        break
                    x += dirs[k][0]
                    y += dirs[k][1]
                    res = max(res, x * x + y * y)
        return res


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = 0
        k = 0
        x, y = 0, 0
        obs = set(map(tuple, obstacles))
        for c in commands:
            if c == -2:
                k = (k - 1) % 4
            elif c == -1:
                k = (k + 1) % 4
            elif 1 <= c <= 9:
                for i in range(c):
                    if (x + dirs[k][0], y + dirs[k][1]) in obs:
                        break
                    x, y = x + dirs[k][0], y + dirs[k][1]
                    res = max(x * x + y * y, res)
        return res


def main():
    sol = Solution()

    commands = [4, -1, 3]
    obstacles = []
    res = sol.robotSim(commands, obstacles)
    print(res)

    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    res = sol.robotSim(commands, obstacles)
    print(res)


if __name__ == '__main__':
    main()
