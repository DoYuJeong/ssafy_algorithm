# T = int(input())
# for tc in range(1,T+1):
#     E, N = map(int, input().split())
#     arr = list(map(int,(input().split())))
#
#     tree = [[] for _ in range(E + 2)]
#     for i in range(0,len(arr),2):
#         p = arr[i]
#         c = arr[i+1]
#         tree[p].append(c)

def postorder(T):
    if T == 0:
        return 0
    l = postorder(left[T])
    r = postorder(right[T])
    return l + r + 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1   # 정점 개수 = 간선 수 + 1

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    cnt = postorder(N)
    print(f'#{tc} {cnt}')
