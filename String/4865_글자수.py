import sys
sys.stdin = open('글자수_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    # str1에 포함된 글자들이 str2에 몇개씩 들어있는지
    str1 = input()
    str2 = input()

    max_result = 0

    for i in str1:
        result = 0
        for j in str2:
            # 같으면 result에 1추가
            if i == j:
                result += 1
        if max_result < result:
            max_result = result
    print(f'#{tc} {max_result}')
