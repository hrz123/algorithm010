# 5466. 最多的不重叠子字符串.py
from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        ss = [ord(c) - ord('a') for c in s]

        lb = [int(1e9)] * 26
        ub = [-1] * 26

        for i, j in enumerate(ss):
            lb[j] = min(lb[j], i)
            ub[j] = max(ub[j], i)

        ln = [-1] * 26
        st = [0] * 26
        for i in range(26):
            x, y = lb[i], ub[i]
            if y < 0:
                continue
            # print(chr(i+ord('a')),x,y)

            while True:
                nx, ny = x, y

                for j in ss[x:y + 1]:
                    nx = min(lb[j], nx)
                    ny = max(ub[j], ny)

                # print((x,y),(nx,ny))
                if nx == x and ny == y:
                    break

                x, y = nx, ny
            st[i] = x
            ln[i] = y - x

        res = []
        mask = []
        for z, x in sorted(list(zip(ln, st))):
            if z < 0:
                continue
            y = x + z
            overlap = False
            for u, v in mask:
                if v < x or y < u:
                    continue
                overlap = True
                break
            if overlap:
                continue
            mask.append((x, y))
            res.append(''.join([chr(i + ord('a')) for i in ss[x:y + 1]]))

        return res


def main():
    sol = Solution()

    s = "adefaddaccc"
    res = sol.maxNumOfSubstrings(s)
    print(res)


if __name__ == '__main__':
    main()
