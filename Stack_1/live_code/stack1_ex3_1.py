'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    print(v)
    visited[v] = 1
    # v에 인접하고 방문안한 w
    for w in adj_list[v]: # 저장한 순서대로...
        if visited[w] == 0: # 방문안한곳
            dfs(w)

V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]
visited = [0] * (V + 1)  # 방문 여부 저장 (0=미방문, 1=방문)

for i in range(E):
    v,w = graph[i*2], graph[i*2+1]

    adj_list[v].append(w)
    adj_list[w].append(v) # 방향이 없는 경우 추가

dfs(1)  # 1번 정점부터 탐색 시작