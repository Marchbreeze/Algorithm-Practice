'''
<9017. 크로스 컨트리>
실버3
https://www.acmicpc.net/problem/9017
'''

# https://velog.io/@o_joon_/BOJ-9017-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%AC%EB%A1%9C%EC%8A%A4-%EC%BB%A8%ED%8A%B8%EB%A6%AC
# 리스트 활용 배우기 ... defaultDict 사용하기

# 한 팀은 6명의 선수로 구성되며, 팀 점수는 상위 4명의 주자의 점수를 합하여 계산
# 6명의 주자가 참가하지 못한 팀은 점수 계산에서 제외
# 결승점을 통과한 순서대로 점수를 받고, 점수를 더하여 가장 낮은 점수를 얻는 팀이 우승
# 동점의 경우에는 다섯 번째 주자가 가장 빨리 들어온 팀이 우승

import sys
from collections import Counter, defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    rank = list(map(int, input().split()))
    cnt = Counter(rank)								# 참가 인원의 수를 세기 위한 Counter
    team = defaultdict(list)						# 각 팀 별 점수 저장을 위한 dictionary
    total, ans = defaultdict(int), defaultdict(int)	# 각 팀 별 총 점수와 정답을 찾기 위한 dictionary
    score = 1										# 들어온 순서대로의 점수

    for i in rank:
        if cnt[i] > 5:					# 현재 팀의 참가 인원이 6명인 경우
            if len(team[i]) < 5:		# 5등까지의 점수만 필요하기 때문에 범위 설정
                team[i].append(score)	# 팀 별 점수 저장
            if len(team[i]) < 5:		# 4등까지의 통합 점수 비교를 위한 범위 설정
                total[i] += score		
            score += 1					# 점수 증가
    
    min_score = min(total.values())		# 총 점수 중 가장 낮은 점수
    for k, v in total.items():
        if v == min_score:
            ans[k] = team[k][-1]		# 가장 낮은 점수인 경우에 해당 팀의 5번째 선수를 ans에 추가
	
    # ans에서 5번째 선수를 기준으로 정렬 후 가장 점수가 낮은 팀 출력
    print(sorted(ans.items(), key=lambda x: x[1])[0][0])