import sys
from collections import deque

def solve():
    # M: 열, N: 행
    m, n = map(int, sys.stdin.readline().split())
    
    # 창고 정보
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    # 익은 토마토들의 위치를 큐에 저장
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
    
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 상자 범위를 벗어나지 않고 익지 않은 토마토(0)인 경우에만 전이
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    # 이전 토마토 날짜 + 1 하여 익게 함
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    
    # 결과 계산
    max_days = 0
    for row in graph:
        for tomato in row:
            # 하나라도 안 익은 게 있다면 -1 반환
            if tomato == 0:
                print(-1)
                return
            max_days = max(max_days, tomato)
    
    print(max_days - 1)

if __name__ == "__main__":
    solve()