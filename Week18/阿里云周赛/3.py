# 3.py

class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation(self, s):
        # write your code here
        li = list(s)
        li.sort()
        q, nq = [""], []
        for char in li:
            for ans in q:
                for i in range(len(ans), -1, -1):
                    if i < len(ans) and char == ans[i]:
                        break
                    nq.append(ans[:i] + char + ans[i:])
            q, nq = nq, []
        q.sort()
        return q


def main():
    sol = Solution()
    s = "aabb"
    res = sol.stringPermutation(s)
    print(res)


if __name__ == '__main__':
    main()
