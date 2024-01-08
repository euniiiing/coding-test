import sys
input = sys.stdin.readline

N, D = map(int, input().split())
dic = {}
for _ in range(N):
    S, E, L = map(int, input().split())
    if S not in dic:
        dic[S] = [(E, L)]
    else:
        dic[S].append((E, L))

answer = [i for i in range(D + 1)]
for i in range(0, D + 1):
    answer[i] = min(answer[i], answer[i - 1] + 1)
    if i in dic:
        for E, L in dic[i]:
            if E > D: continue
            answer[E] = min(answer[E], answer[i]+ L)

print(answer[D])