'''
<15686. 치킨 배달>
골드5
https://www.acmicpc.net/problem/15686
'''

# 크기가 N×N인 도시, 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나 (0은 빈 칸, 1은 집, 2는 치킨집)
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리, 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|
# 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성

# N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
n, m = map(int, input().split())

# 도시 정보
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

# 치킨집, 빈집 탐색
chicken, house = [], []
for y in range(n):
    for x in range(n):
        if city[y][x] == 1:
            house.append((y,x))
        elif city[y][x] == 2:
            chicken.append((y,x))

# M개의 치킨집 조합 백트래킹으로 탐색
stack = [([],0)] # 예비조합, 인덱스
total = len(chicken)
choice = []
while stack:
    saved, idx = stack.pop()
    if len(saved) == m:
        choice.append(saved)
        continue
    for i in range(idx,total):
        stack.append((saved + [chicken[i]], i+1))

# M개 조합 비교
result = 1e9
for c in choice:
    citydist = 0
    for h in house:
        housedist = 1e9
        for i in range(m):
            housedist = min(housedist, abs(c[i][0] - h[0]) + abs(c[i][1] - h[1]))
        citydist += housedist
    result = min(result, citydist)

print(result)