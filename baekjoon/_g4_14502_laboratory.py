'''
<14502. 연구소>
골드4
https://www.acmicpc.net/problem/14502
'''

# 문제 : N×M인 직사각형 연구소에 빈칸(0), 벽(1), 바이러스(2)가 존재함 / 벽 3개를 설치하여 바이러스가 퍼지는 공간 최소화
# note:
# 1. 바이러스는 상하좌우의 인접한 빈칸으로 이동하므로 bfs로 카운트 (바이러스의 위치를 큐에 전부 넣고 while queue)
# 2. 벽을 꼭 3개를 세워야하므로 벽을 3개 세웠을 때 바이러스를 퍼트려보고 개수 카운트 (모든 경우 - 재귀함수로 맵 재활용 !!)

from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 1. 벽만들기
def make_wall(count):
    # 벽 3개 생성 완료 시 bfs 호출
    if count == 3:
        bfs()
        return
    
    # 모든 0에 대해서 벽
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] == 0:
                # 벽 생성
                lab_map[i][k] = 1
                # count +1한 재귀함수 호출
                make_wall(count+1)
                # 밖으로 나왔을 땐 다시 0(빈칸)으로
                lab_map[i][k] = 0


# 2. 바이러스 영역 구하기
def bfs():
    queue = deque()
    # map에 deepcopy 적용 후, 바이러스 위치 전부 append
    test_map = copy.deepcopy(lab_map)
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 2:
                queue.append((i,k))

    # bfs 진행
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            dr = r+dx[i]
            dc = c+dy[i]
            if (0<=dr<n) and (0<=dc<m):
                if test_map[dr][dc] == 0:
                    test_map[dr][dc] = 2
                    queue.append((dr,dc))

    # 바이러스 개수 카운트
    global result
    count = 0
    for i in range(n):
        for k in range(m):
            if test_map[i][k] == 0:
                count += 1
    result = max(result, count)


result = 0
make_wall(0)
print(result)