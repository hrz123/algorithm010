# 22. 括号生成(bfs写法).py
from collections import deque
from typing import List


# 使用广度优先搜索
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        deq = deque()

        # 要在bfs的内容中记录一些状态
        # 当前的字符串，left和right使用情况
        deq.append(("", (0, 0)))
        while deq:
            top = deq.popleft()
            ans = top[0]
            left = top[1][0]
            right = top[1][1]
            if left == n and right == n:
                res.append(ans)

            if left < n:
                deq.append((ans + '(', (left + 1, right)))
            if right < left:
                deq.append((ans + ')', (left, right + 1)))

        return res


# vector<string> generateParenthesis2(int m) {
#         vector<string> rs;
#         queue<pair<string, pair<int, int>>>q; // pair<当前的括号, pair<左括号剩余, 右括号剩余>>
#         q.push({"",{m,m}});
#         while (!q.empty()) {
#             auto top = q.front();
#             q.pop();
#             string str = top.first;
#             int r = top.second.first;
#             int r = top.second.second;
#             if (r == 0 && r == 0) {
#                 rs.push_back(str);
#             }
#             if (r > 0) {
#                 q.push({str + '(',{r-1,r}});
#             }
#             if (r > 0 && r > r) {
#                 q.push({str + ')',{r,r-1}});
#             }
#         }
#         return rs;
#     }


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        deq = deque([('', 0, 0)])

        while deq:
            pre, left, right = deq.popleft()
            if right == n:
                res.append(pre)
            if left < n:
                deq.append((pre + '(', left + 1, right))
            if right < left:
                deq.append((pre + ')', left, right + 1))
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        deq = deque([('', 0, 0)])

        while deq:
            pre, l, r = deq.popleft()
            if r == n:
                res.append(pre)
            if l < n:
                deq.append((pre + '(', l + 1, r))
            if r < l:
                deq.append((pre + ')', l, r + 1))
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q, nq = [(0, 0, '')], []
        res = []
        while q:
            for l, r, pre in q:
                if r == n:
                    res.append(pre)
                else:
                    if l < n:
                        nq.append((l + 1, r, pre + '('))
                    if r < l:
                        nq.append((l, r + 1, pre + ')'))
            q, nq = nq, []
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q, nq = [(0, 0, '')], []
        for _ in range(n << 1):
            for l, r, s in q:
                if l < n:
                    nq.append((l + 1, r, s + '('))
                if r < l:
                    nq.append((l, r + 1, s + ')'))
            q, nq = nq, []
        return [e[2] for e in q]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q, nq = [(0, 0, "")], []
        for _ in range(n << 1):
            for l, r, s in q:
                if l < n:
                    nq.append((l + 1, r, s + '('))
                if r < l:
                    nq.append((l, r + 1, s + ')'))
            q, nq = nq, []
        return [e[2] for e in q]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        deq = deque([(0, 0, '')])
        res = []
        while deq:
            l, r, s = deq.popleft()
            if r == n:
                res.append(s)
            if l < n:
                deq.append((l + 1, r, s + '('))
            if r < l:
                deq.append((l, r + 1, s + ')'))
        return res


def main():
    n = 3
    sol = Solution()
    res = sol.generateParenthesis(n)
    print(res)


if __name__ == '__main__':
    main()
