import sys
sys.stdin = open("1974_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result = 0

    # 가로 확인
    for i in range(9):
        row = []
        for j in range(9):
            row.append(arr[i][j])
        check_row = set(row)
        if len(check_row) != 9:
            break
        print(check_row)
    # 세로 확인


    # 3X3 확인
    
