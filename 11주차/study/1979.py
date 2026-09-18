import sys
sys.stdin = open("1979_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    # 가로 줄 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1: # 1을 만나면 연속된 1 개수 + 1
                cnt += 1
            else: # 0을 만나면 지금까지 연속된 개수가 K개인지 확인하고 cnt = 0
                if cnt == K:
                    result += 1
                cnt = 0
        # i번째 가로줄이 끝났을 때 확인
        if cnt == K:
            result += 1

    # 세로줄 확인
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1: # 1을 만나면 연속된 1 개수 + 1
                cnt += 1
            else: # 0을 만나면 지금까지 연속된 개수가 K개인지 확인하고 cnt = 0
                if cnt == K:
                    result += 1
                cnt = 0
        # i번째 세로줄이 끝났을 때 확인
        if cnt == K:
            result += 1

    print(f'#{tc} {result}')