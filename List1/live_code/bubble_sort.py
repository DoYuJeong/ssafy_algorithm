# 거품정렬
# [5,2,3,1,4]
# >> [1,2,3,4,5]
# 2개씩 비교해서 큰거 보내는 작업 * N번
# 2개씩 비교해서 큰거 뒤로 보내기
arr = [5,2,3,1,4]
N = len(arr)
for j in range(N-1): # i 범위는 0번부터 N-2번까지 해야지 뒤에 두개 비교가능
    for i in range(N-1-j):
        # i번과 i+1번 비교해서 i번이 크면 자리 바꿔주기
        if arr[i] > arr[i+1]:
            # arr[i+1], arr[i] = arr[i], arr[i+1]
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            # 자리 바꿔주기
print(arr)

# 카운팅정렬
# 스킬 >>
# 값을 배열의 인덱스로 사용하기
a = [1,4,3,2,1,1,3,4,5]
# a의 요소가 각 몇 번 나왔는지 세는 배열
b = [0] * 10 # 0번부터 9번 인덱스까지 존재

for i in range(len(a)):
    # a[i] # a의 요소
    b[a[i]] += 1

print(b)