'''
<1992. 쿼드트리>
실버1
https://www.acmicpc.net/problem/1992
'''

n = int(input())
array = [list(input()) for _ in range(n)]
answer = ""

def divide_and_conquer(length: int, square: list):
    global answer
    total = 0
    for i in range(length):
        for j in range(length):
            total += int(square[i][j])
    if total == 0:
        answer += "0"
    elif total == length**2:
        answer += "1"
    else:
        answer += "("
        divide_and_conquer(length//2, [square[i][0:length//2] for i in range(0, length//2)])
        divide_and_conquer(length//2, [square[i][length//2:length] for i in range(0, length//2)])
        divide_and_conquer(length//2, [square[i][0:length//2] for i in range(length//2, length)])
        divide_and_conquer(length//2, [square[i][length//2:length] for i in range(length//2, length)])
        answer += ")"

divide_and_conquer(n, array)
print(answer)