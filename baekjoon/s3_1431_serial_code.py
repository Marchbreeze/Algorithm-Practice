'''
<1431. 시리얼 번호>
실버3
https://www.acmicpc.net/problem/1431
'''

n = int(input())
array = []
for _ in range(n):
    code = input()
    sum_num = 0
    for letter in code:
        if (letter.isdigit()):
            sum_num += int(letter)
    array.append((code, len(code), sum_num))

array.sort(key=lambda x: (x[1], x[2], x[0]))
for code in array:
    print(code[0])