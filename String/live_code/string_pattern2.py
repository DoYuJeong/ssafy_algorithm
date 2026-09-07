t = 'TTTTTATTAATA'
p = 'TAA'

def search(p,t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1): # 비교 구간 시작 i
        for j in range(M): # 패턴 내부 비교 위치 j
            if t[i+j] != p[j]: # 다르면 다음 구간으로...
                continue # for j로 돌아감(현재 반복문의 앞으로 돌아가는 것)
                # break # for j(현재 반복문을 깨고 나가는 것)
        else: # for j가 정상 종료
            return i
    return -1 # 일치하는 패턴 없음
print(search(p,t))
