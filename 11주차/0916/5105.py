def bfs(i, j, N):
    # 초기화
    visited = [[0]*N for _ in range(N)] # visited 생성
    q = [(i, j)] # 큐 생성
    # 시작점 인큐
    visited[i][j] = 1 # 시작점 인큐 표시
    # 반복
    while q:
        ti, tj = q.pop(0) # 디큐
        if maze[ti][tj] == '3': # 처리
            return  visited[ti][tj] - 2
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!='1' and visited[ni][nj] == 0:  # 인접칸이 벽이 아니고 인큐한 적이 없으면
                q.append((ni, nj)) # 인큐, 인큐표시
                visited[ni][nj] == visited[ti][tj] + 1
        return 0

def find_start(maze,N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    si, sj = find_start(maze,N)
    ans = bfs(si,sj,N)
    print(f'#{tc} {ans}')