T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 사각형 영역 N 개
    arr = [[0] * 10 for _ in range(10)] # 10X10 크기의 격자 생성, 0으로 초기화
    # 보라색 영역 개수
    result = 0

    for i in range(N):
        # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color
        # (r1, c1): 사각형의 왼쪽 위 모서리 좌표 (행, 열)
        # (r2, c2): 사각형의 오른쪽 아래 모서리 좌표
        r1, c1, r2, c2, color = map(int, input().split())
        # 격자에 빨간색이면 1 추가, 파란색이면 2 추가 -> 값이 3인 격자 = 보라색
        # 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color
                if arr[i][j] == 3:
                    result += 1
    print(f'#{tc} {result}')