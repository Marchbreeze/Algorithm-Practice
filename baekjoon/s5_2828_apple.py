'''
<2828. 사과 담기 게임>
실버5
https://www.acmicpc.net/problem/2828
'''

# 스크린 칸 N, 바구니 크기 M
n, m = map(int, input().split())

# 사과 개수 j
j = int(input())

# 바구니의 왼쪽 : 0 ~ n-m
# 왼쪽, 오른쪽 위치 따라 가기
basket = 1
result = 0
for _ in range(j):
    apple = int(input())
    if (apple > (basket + m - 1)):
        result += apple - basket - m + 1
        basket += apple - basket - m + 1
    elif (apple < basket):
        result += basket - apple
        basket -= basket - apple

print(result)