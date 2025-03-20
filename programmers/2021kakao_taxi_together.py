def solution(n, s, a, b, fares):
    
    # 지점 2차원 그래프 설정
    graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
    
    # 자기 자신 비용 0 설정
    for i in range(1,n+1):
        graph[i][i] = 0
    
    # 지점 양방향 연결 및 비용 설정
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    
    # 플로이드-워셜 진행
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
    # S-C + C-A + C-B 최소값 찾기
    answer = int(1e9)
    for i in range(1,n+1):
        answer = min(answer, graph[s][i]+graph[i][a]+graph[i][b])
    
    return answer