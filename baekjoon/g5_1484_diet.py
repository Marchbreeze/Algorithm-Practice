'''
<1484. 다이어트>
골드5
https://www.acmicpc.net/problem/1484
'''

# g까지 투포인터로 각 숫자의 제곱차가 g일때까지 구하기

g = int(input())

start = 1
end = 1
count = 0

while end <= g:
    gap = end**2 - start**2
    if gap == g:
        print(end)
        count += 1
        end += 1
    elif gap < g:
        end += 1
    else:
        start += 1

if (count == 0):
    print(-1)