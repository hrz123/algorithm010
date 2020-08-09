学习笔记

## 动态规划题目串讲

##### 爬楼梯

##### 不同路径1&2

##### 打家劫舍1&2&3

dp[i] = max(dp[i-2] + nums[i], dp[i-1])

max$ of robbing A[0->i] 且没偷 nums[i]

dp[i] [0] = max(dp[i-1] [0], dp[i-1] [1])

dp[i] [1] = dp[i-1] [0] + nums[i]

##### 最小路径

##### 不同路径2 递推方程

dp[i] [j] = dp[i+1] [j] + dp[i] [j + 1] if board[i] [j] = 0

dp[i] [j] = 0                                       elif board[i] [j] = 1

##### 背包问题解决办法