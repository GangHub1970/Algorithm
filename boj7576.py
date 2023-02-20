from collections import deque

def bfs():
    global zero
    q = deque(tomato)

    while q:
        now = q.popleft()
        r, c = now[0], now [1]

        for i in range(4):
            if r + dr[i] < n and c + dc[i] < m and r + dr[i] >= 0 and c + dc[i] >= 0:
                nr = r + dr[i]
                nc = c + dc[i]
                if box[nr][nc] == 0:
                    q.append((nr, nc))
                    box[nr][nc] = box[r][c] + 1
                    zero -= 1


m, n = map(int, input().split())

box = []
zero = 0
for _ in range(n):
    row = list(map(int, input().split()))
    zero += row.count(0)
    box.append(row)

tomato = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append((i, j))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
bfs()

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, box[i][j])

if zero != 0:
    print(-1)
else:
    print(result - 1)