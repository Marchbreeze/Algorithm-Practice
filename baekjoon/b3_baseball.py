'''
<10214. Baseball>
브론즈3
https://www.acmicpc.net/problem/10214
'''

t = int(input())

for _ in range(t):
    yonsei = 0
    korea = 0
    for i in range(9):
        y, k = map(int, input().split())
        yonsei += y
        korea += k
    if (yonsei > korea):
        print("Yonsei")
    elif (yonsei == korea):
        print("Draw")
    else:
        print("Korea")