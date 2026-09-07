arr = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [2,4,6,8,10],
    [1,3,5,7,9],
    [10,8,6,4,2]
]

di = [-1,-1,1,1]
dj = [-1,1,-1,1]


max_v = 0
for i in range(N):
    for j in range(N):
        sum_v = arr[i][j]
        for d in range(4):
            ni = i + di[d]*k
            nj = j + dj[d]*k
            if 0 <= ni < N and 0 <= nj < N:
                sum_v += arr[ni][nj]
        if sum_v > max_v:
            max_v = sum_v
print(sum_v)
