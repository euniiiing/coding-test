import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []
players = []
for _ in range(p):
    ll, n = input().split()
    l = int(ll)

    r = False
    for idx, room in enumerate(rooms):
        if room[1] == m: continue

        if l >= room[0] - 10 and l <= room[0] + 10:
            room[1] += 1
            players[idx].append([n, l])
            r = True
            break
    
    if not r:
        rooms.append([l, 1])
        players.append([[n, l]])

for idx, room in enumerate(rooms):
    if room[1] < m: print("Waiting!")
    else: print("Started!")
    for player in sorted(players[idx]):
        print(player[1], player[0])
