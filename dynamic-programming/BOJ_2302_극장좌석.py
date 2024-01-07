import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
is_vip = [0] * (N + 1)
for _ in range(M):
    is_vip[int(input())] = 1

dp = [[0, 0] for _ in range(N + 1)]
dp[1] = [1, 0]
for i in range(2, N + 1):
    if is_vip[i]:
        dp[i][0] = sum(dp[i - 1])
        continue

    if not is_vip[i - 1]:
        dp[i][1] = dp[i - 1][0]
    dp[i][0] = sum(dp[i - 1])

print(sum(dp[N]))

    