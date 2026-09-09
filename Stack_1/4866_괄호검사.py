# 문자열에서 괄호 (), {} 가 정상적으로 짝을 이루는지 검사하는 문제
# 가장 최근에 열린 괄호부터 먼저 닫혀야 한다는 성질 -> stack

import sys
sys.stdin = open('괄호검사_input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    s = input() # 입력받은 문자열
    stack = []  # 여는 괄호를 담을 stack
    result = 0  # 괄호 검사

    for c in s:
        if c in '{(':   # 여는 괄호는 stack에 넣는다.
            stack.append(c)
        elif c in '})': # 닫는 괄호를 stack 값과 확인
            # 스택이 비어있지 않아야 하고 입력받은 문자와 stack의 top이랑 비교해서 괄호가 맞다면 제거
            if stack and ((stack[-1] == '{' and c == '}') or (stack[-1] == '(' and c == ')')):
                stack.pop() # 짝이 맞으면 스택에서 제거
            else:   # 괄호의 짝이 맞지 않거나, 여는 괄호가 없다면 break
                break
    else: # for문이 break 없이 끝까지 다 돌았을 때만 이 블록이 실행됨
        if not stack:   # 여는 괄호가 다 닫혔는지 확인
            result = 1
    print(f'#{tc} {result}')


