T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 전선의 개수, 1 ≤ N ≤1000
    AB = [list(map(int, input().split())) for _ in range(N)]

    AB.sort()
    cnt = 0
    for i in range(1,N):
        for j in range(i):
            if AB[j][1] > AB[i][1]:
                cnt += 1

    print(f'#{tc} {cnt}')