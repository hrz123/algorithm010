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


# vector<string> generateParenthesis2(int n) {
#         vector<string> rs;
#         queue<pair<string, pair<int, int>>>q; // pair<当前的括号, pair<左括号剩余, 右括号剩余>>
#         q.push({"",{n,n}});
#         while (!q.empty()) {
#             auto top = q.front();
#             q.pop();
#             string str = top.first;
#             int left = top.second.first;
#             int right = top.second.second;
#             if (left == 0 && right == 0) {
#                 rs.push_back(str);
#             }
#             if (left > 0) {
#                 q.push({str + '(',{left-1,right}});
#             }
#             if (right > 0 && right > left) {
#                 q.push({str + ')',{left,right-1}});
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


def main():
    n = 3
    sol = Solution()
    res = sol.generateParenthesis(n)
    print(res)


if __name__ == '__main__':
    main()
