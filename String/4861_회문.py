import sys
sys.stdin = open('회문_input.txt','r')

def a(N,M,str):
    for i in range(N):
        k = 9
        # k는 M글자짜리 구간이 시작하는 위치
        for k in range(N-M+1):
            # 가로 회문
            row = str[i][k:k+M]
            # 세로 회문
            col = [str[j][i] for j in range(k,k+M)]
            # 자신과 자신을 뒤집은 것이 같다면 회문
            if row == row[::-1]:
                return row
            if col == col[::-1]:
                return col

# T : 테스트 케이스 개수
T = int(input())
for tc in range(1,T+1):
    # N : N*N 크기의 글자판, M : 회문의 길이
    N, M = map(int,input().split())
    # str : NxN 글자판
    str = [input() for _ in range(N)] # NxN 글자판

    result = a(N,M,str)
    print(f'#{tc}',''.join(result))
