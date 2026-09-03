import sys
sys.stdin=open("sum_input.txt","r")

for _ in range(10):
    tc = int(input())  # 테스트케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100x100 배열
    # print(arr)

    max_sum = arr[0][0]  # 계산 결과

    # 1. 각 행의 합
    for i in range(100):
        row_sum = 0 # 각 행마다 합계산할 때 0으로 초기화
        for j in range(100):
            row_sum += arr[i][j]
        if row_sum > max_sum:
            max_sum = row_sum

    # 2. 각 열의 합
    for j in range(100):
        line_sum = 0 # 각 열마다 합계산할 때 0으로 초기화
        for i in range(100):
            line_sum += arr[i][j]
        if line_sum > max_sum:
            max_sum = line_sum

    # 3. 각 대각선의 합
    a = 0
    for i in range(100):
        a += arr[i][i]
    if a > max_sum:
        max_sum = a

    b = 0
    for i in range(100):
        b += arr[i][100-1-i]
    if b > max_sum:
        max_sum = b

    print(f'#{tc} {max_sum}')

