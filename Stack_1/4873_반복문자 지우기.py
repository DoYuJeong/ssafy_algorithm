# 문자열에서 인접한 같은 문자를 반복적으로 제거하고, 남은 문자열의 길이를 구하는 문제

import sys
sys.stdin = open('반복문자_input.txt','r')

def solve(s):
    stack = []
    for ch in s:
        # 1.스택이 비어있지 않고, 스택의 top이 지금 글자(ch)와 같다면 pop
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            # 2. 비어있거나 top과 같지않으면 push
            stack.append(ch)
    # 3. 반복이 끝나면 스택에 남은 결과
    return ''.join(stack)

T = int(input())
for tc in range(1,T+1):
    arr = input()
    result = solve(arr)
    print(f'#{tc} {len(result)}')