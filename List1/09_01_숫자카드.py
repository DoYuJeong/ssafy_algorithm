import sys
sys.stdin=open("venv/input.txt","r")

T = int(input()) # 테스트 케이스 개수  1 ≤ T ≤ 50
for tc in range(1,T+1):
    N = int(input()) # 카드 장수  5 ≤ N ≤ 100
    card_str = input() # N개의 숫자 0 ≤ ai ≤ 9

    cnt = [0] * 10  # 숫자가 몇 번 나왔는지 셀 배열

    # 1. 문자열을 한 글자씩 순회하며 개수 세기
    for str in card_str:
        num = int(str)  # 문자 하나를 숫자로 변환
        cnt[num] += 1 # cnt 리스트에서 num번째 칸의 값을 +1

    # 2. cnt 배열에서 최댓값과 그 숫자 찾기
    max_count = 0
    max_num = 0
    for i in range(10):
        if cnt[i] >= max_count:
            max_count = cnt[i]
            max_num = i

    print(f'#{tc} {max_num} {max_count}')