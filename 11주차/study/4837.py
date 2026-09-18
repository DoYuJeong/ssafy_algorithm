import sys
sys.stdin = open("4837_input.txt", "r")
# 1) combinations 사용
import itertools

# T = int(input())
# A = [i for i in range(1,13)]
#
# for tc in range(1,T+1):
#     N, K = map(int,input().split())
#     combi = list(itertools.combinations(A,N))
#     cnt = 0
#     for i in combi:
#         if sum(i) == K:
#             cnt += 1
#     print(f'#{tc} {cnt}')

# 2) 재귀함수 사용
def dfs(n,sum,cnt):
    global ans
    # 가지치기
    if sm>K:
        return

    # 종료조건: n에 관련된 수식
    if n == A:
        if cnt == N and sum ==K:
            ans += 1
        return

    # 사용 O
    dfs(n+1,sum+lst[n],cnt+1)
    # 사용 X
    dfs(n+1,sum,cnt)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    lst = [n for n in range(1, 13)]
    A = 12

    ans = 0
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')
