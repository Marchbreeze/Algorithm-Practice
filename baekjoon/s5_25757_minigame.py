'''
<25757. 임스와 함께하는 미니게임>
실버5
https://www.acmicpc.net/problem/25757
'''

# 게임 종류 : 2인용 Y, 3인용 F, 4인용 O
# 플레이어 당 한번씩만, 최대 횟수?

# 신청횟수, 게임종류 입력
n, game = input().split()
n = int(n)
if (game == "Y"):
    game = 1
elif (game == "F"):
    game = 2
else:
    game = 3

# 집합 자료형에 플레이어 담기
players = set()
for _ in range(n):
    player = input().strip()
    players.add(player)

# 최대 게임 출력
print(len(players) // game)