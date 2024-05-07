'''
<2847. 게임을 만든 동준이>
실버4
https://www.acmicpc.net/problem/2847
'''

# 입력
n = int(input())
array = []
for i in range(n):
    num = int(input())
    array.append(num)

# 재귀함수
def check(i, array):
    global count
    if (array[i] >= array[i+1]):
        count += array[i] - array[i+1] + 1
        array[i] = array[i+1] - 1
    if (i != 0):
        check(i-1, array)

count = 0
for i in range(n-1):
    check(i, array)

print(count)