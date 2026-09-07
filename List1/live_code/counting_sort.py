# 1. 요소의 개수세기
# 2. 누적합 구하기(내자리 계산하기)
# 3. 자리 찾아서 넣어주기
arr = [4, 6, 7, 8, 2, 2, 5, 7, 9, 8, 3, 4, 7, 8, 3, 1, 5]
N = len(arr)
cnt = [0] * 10
sorted_arr = [0]*N
# 1. 요소 개수 세기
for i in range(N):
    num = arr[i]
    cnt[num] += 1
# 2. 누적합 구하기
for i in range(1,10): # 0번은 누적합 계산X
    # 앞 인덱스 값과 현재 인덱스 값 더해서 현재 인덱스에 재할당
    cnt[i] = cnt[i-1] + cnt[i]
# 3. 제 위치에 맞게 넣어주기
# 원본 arr의 요소가 들어갈 위치를 cnt 배열에서 확인하고 sorted_arr에 넣어주기
for i in range(N):
    num = arr[i]
    cnt[num] -= 1 # 들어갈 순번을 인덱스로 변경하기 및 다음 값 순번 계산
    idx = cnt[num]
    sorted_arr[idx] = num
    # sorted_arr[cnt[arr[i]-1]] = arr[i]
    # cnt[arr[i]] -= 1

print(sorted_arr)