# N 정류장 수, K 한 번 충전으로 최대 이동할 수 있는 정류장 수, 충전기가 설치된 M개의 정류장 번호

# 충전횟수가 최소가 되도록 충전 -> 가능한 멀리서 충전
# 현재 위치에서 갈 수 있는 위치에 충전소가 있는지 확인
# 없으면 뒤로 되돌아 가면서 충전하기


# 표준입력 스트림: 터미널로 기본 설정 되어있음
import sys
sys.stdin=open("전기버스_input.txt","r")

# 노선 수 T
T = int(input())
for tc in range(1,T+1):
    # k 충전량, N 정류장 개수, M 충전기 개수
    K,N,M = map(int, input().split())
    charger = list(map(int,input().split()))
    # 정류장에 충전소가 있으면 1, 없으면 0
    stations = [0] * (N+1)
    for idx in charger:
        stations[idx] = 1
    # for i in range(M):
    #     stations[charger[i]] = 1
    # print(stations)
    # 현재 위치에서 갈 수 있는 거리부터 충전소가 있는지 검사 없으면 되돌아 가기
    # 충전기가 있으면 충전하기 >> 반복! 목적지에 도착할 때 까지 반복
    position = 0  # 현재위치
    cnt = 0  # 충전 횟수 세시 변수
    while position + K < N:  # 충전기 찾아서 충전하기 반복
        # 갈 수 있는데 까지 가서 되돌아 오면서 찾기
        is_find = False
        for next in range(position+K,position,-1):
            if stations[next] == 1: # 충전기 있는지 확인
                cnt += 1 # 충전하고 다음충전소 찾기
                position = next
                is_find = True
                break # 돌아가면서 찾기 종료
        # 충전소 찾는 반복문에서 충전소 찾았니?
        if is_find == False:
            cnt = 0 # 목적지 도착 못 할 경우 0 출력
            break
    print(f'#{tc} {cnt}')
