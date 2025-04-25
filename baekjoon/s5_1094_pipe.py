'''
<1094. 막대기>
실버5
https://www.acmicpc.net/problem/1094
'''

x = int(input())
array = [64]

while True:
    total = 0
    for pipe in array:
        total += pipe
    if total <= x:
        break
    short = array.pop()
    half = short // 2
    array.append(half)
    if total - half < x:
        array.append(half)

print(len(array))