import sys
input = sys.stdin.readline

for _ in range(int(input())):
    T, *std_h = map(int, input().split())
    answer = 0
    result = []

    for std in std_h:
        rank = -1

        for i, friend in enumerate(result):
            if friend > std:
                rank = i
                break

        if rank == -1:
            result.append(std)
        else:
            answer += len(result) - rank
            result = result[:rank] + [std] + result[rank:]

    print(T, answer)