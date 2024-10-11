'''
<14889. 스타트와 링크>
실버1
https://www.acmicpc.net/problem/14889
'''

# 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수
# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치
# 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji
# 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력

'''
1은 고정
10명이면 4명 뽑아 5명 점수 계산 & 나머지 계산
'''

# 전체인원 N
n = int(input())

# 능력치 (인덱스 0부터 -> 1번은 s[0])
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

# 백트래킹으로 숫자 n/2-1개 뽑기
teams = []
stack = [(2,[])]
while stack:
    idx, saved = stack.pop()
    if len(saved) == n/2-1:
        saved.append(1)
        teams.append(saved)
        continue
    for i in range(idx,n+1):
        stack.append((i+1, saved +[i]))

# 팀 총합 차이 구하기
result = 1e9
for team_1 in teams:
    # 1팀 총합
    score_1 = 0
    for i in range(n//2):
        for j in range(i+1,n//2):
            score_1 += s[team_1[i]-1][team_1[j]-1] + s[team_1[j]-1][team_1[i]-1]
    # 2팀 리스트
    team_2 = []
    for i in range(2,n+1):
        if i not in team_1:
            team_2.append(i)
    # 2팀 총합
    score_2 = 0
    for i in range(n//2):
        for j in range(i+1,n//2):
            score_2 += s[team_2[i]-1][team_2[j]-1] + s[team_2[j]-1][team_2[i]-1]
    # 차이 기록
    result = min(result, abs(score_1 - score_2))
print(result)