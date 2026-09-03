# 연습문제1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    ans += arr[i][i] + arr[i][N-1-i]

if N%2: # N이 홀수인 경우에만 중심 원소가 겹침
    ans -= arr[N//2][N//2]

print(ans)

# 연습문제2
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    for j in range(N):
        s = 0 # i, j 이웃과 차이의 절댓값의 합
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i + di, j + dj # 이웃 원소 인덱스 후보
            if 0<=ni<N and 0<=nj<N: # 존재하는 인덱스면
                s += abs(arr[i][j] - arr[ni][nj])
                # s += arr[i][j] - arr[ni][nj] if arr[i][j] >= arr[ni][nj] else arr[ni][nj]-arr[i][j]
                # tmp = arr[i][j] - arr[ni][nj]
                # tmp = tmp if tmp < 0 else - tmp
                # if tmp<0:
                # tmp *= -1
        total += s
print(total)