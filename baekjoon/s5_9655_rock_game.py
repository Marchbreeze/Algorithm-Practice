'''
<9655. 돌 게임>
실버5
https://www.acmicpc.net/problem/9655
'''

# 1개 : 상 - 1
# 2개 : 창 - 1,1
# 3개 : 상 - 3
# 4개 : 창 - 1,3 / 3,1
# 5개 : 상 - 1,1,3 / 1,3,1
# 6개 : 창 - 1,1,1,3

import sys

# 돌 개수 입력
n = int(sys.stdin.readline())

if n%2==0:
    print('CY')
else:
    print('SK')