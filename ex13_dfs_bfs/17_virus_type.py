'''
< 17. 경쟁적 전염 >
N x N 크기의 시험관에 1~K 번의 바이러스가 존재할 수 있다.
바이러스는 매초 상하좌우로 증식한다.
증식 과정은 번호가 낮은 바이러스부터 진행되며, 특정 칸에 바이러스가 있다면 들어갈 수 없다.
바이러스의 초기 위치 정보가 주어졌을때, S초가 지난 뒤 (X,Y)에 존재하는 바이러스를 구하시오.
(1 <= N <= 200, 1 <= K <= 1,000, 0 <= S <= 10,000)
'''

# 크기, 종류 입력
n, k = map(int, input().split())

# 바이러스 위치 정보 입력
virus = []
for _ in range(n):
    virus.append(list(map(int, input().split())))

# S초가 지난 뒤 (X,Y) 입력
s, x, y = map(int, input().split())

# 방향 설정
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# s번 반복
for _ in range(s):
    # 1부터 바이러스 찾기
    for i in range(1, k+1):
        # 위치 하나씩 탐색
        ith_virus = []
        for a in range(n):
            for b in range(n):
                if (virus[a][b] == i):
                    ith_virus.append((a,b))
        # 주위 탐색하기
        for v in ith_virus:
            for j in range(4):
                nx = v[0] + dx[j]
                ny = v[1] + dy[j]
                if (nx >= 0 and nx < n and ny >= 0 and ny < n):
                    if (virus[nx][ny] == 0):
                        virus[nx][ny] = i

# 결과 출력
print(virus[x-1][y-1])