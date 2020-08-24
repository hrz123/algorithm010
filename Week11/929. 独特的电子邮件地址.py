# 929. 独特的电子邮件地址.py
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mem = set()
        for e in emails:
            x, y = e.split('@')
            if x.find('+') != -1:
                x = x[:x.find('+')]
            x = ''.join(x.split('.'))
            s = x + '@' + y
            if s not in mem:
                mem.add(s)
        return len(mem)


def main():
    sol = Solution()
    emails = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
    res = sol.numUniqueEmails(emails)
    print(res)


if __name__ == '__main__':
    main()
