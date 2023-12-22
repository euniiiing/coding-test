import sys
from heapq import heappop, heappush
input = sys.stdin.readline

T, n = map(int, input().split())
heap = []

for _ in range(n):
    a, b, c = map(int, input().split())
    heappush(heap, (-c, a, b))

while T and heap:
    T -= 1
    rc, a, b = heappop(heap)
    print(a)
    if (b - 1) > 0:
        heappush(heap, (rc + 1, a, b - 1))