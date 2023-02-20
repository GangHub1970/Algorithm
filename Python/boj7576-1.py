from collections import deque
import sys
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:
        now = q.popleft()
        r, c = now[0], now[1]

        for i in range(4):
            if r + dr[i] < n and c + dc[i] < m and r + dr[i] >= 0 and c + dc[i] >= 0:
                nr = r + dr[i]
                nc = c + dc[i]
                if box[nr][nc] >= 0:
                    if box[nr][nc] >= box[r][c] + 1:
                        q.append((nr, nc))
                        box[nr][nc] = box[r][c] + 1


m, n = map(int, input().split())

box = []
for _ in range(n):
    lst = list(map(int, input().split()))
    for i in range(m):
        if lst[i] == 0:
            lst[i] = 9999999
    box.append(lst)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            bfs(i, j)

count = 0
result = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 9999999:
            count += 1
            break
        result = max(result, box[i][j])
    if count > 0:
        break

if count > 0:
    print(-1)
else:
    print(result - 1)


