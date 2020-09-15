# 134. 加油站.py
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t_gas, c_gas = 0, 0
        res = 0
        for i in range(len(gas)):
            t_gas += gas[i] - cost[i]
            c_gas += gas[i] - cost[i]
            if c_gas < 0:
                res = i + 1
                c_gas = 0
        return res if t_gas >= 0 else -1


def main():
    sol = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    res = sol.canCompleteCircuit(gas, cost)
    print(res)


if __name__ == '__main__':
    main()
