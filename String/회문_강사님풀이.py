import sys
sys.stdin = open('회문_input.txt','r')

# data에 길이 M인 회문이 있으면 찾아서 반환하는 함수...
def solve(data):
    # 검사할 문장의 시작점 순회...
    for i in range(N):  # i는 행 번호.. 다 검사해야함..
        for j in range(N-M+1):  # 행 번호는 M보다 작은 뒷쪽은 검사 안함.
            # j 열에서 시작하는 길이 M짜리 회문이 있는지 검사...
            is_find = True
            for k in range(M//2):
                # j+k번, j+M-1-k번과 비교...
                if data[i][j+k] != data[i][j+M-1-k]:
                    is_find = False  # 회문이 아님...
            # 회문이면, 회문 반환...
            if is_find:  # j번부터 j+M-1번까지 회문!
                palindrome = ''
                for l in range(j, j+M):
                    palindrome += data[i][l]
                return palindrome

    for i in range(N):  # i는 행 번호.. 다 검사해야함..
        for j in range(N-M+1):  # 행 번호는 M보다 작은 뒷쪽은 검사 안함.
            # j 열에서 시작하는 길이 M짜리 회문이 있는지 검사...
            is_find = True
            for k in range(M//2):
                # j+k번, j+M-1-k번과 비교...
                if data[j+k][i] != data[j+M-1-k][i]:
                    is_find = False  # 회문이 아님...
            # 회문이면, 회문 반환...
            if is_find:  # j번부터 j+M-1번까지 회문!
                palindrome = ''
                for l in range(j, j+M):
                    palindrome += data[l][i]
                return palindrome

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input().strip() for _ in range(N)]
    result = solve(data)
    print(f'#{tc} {result}')