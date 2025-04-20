'''
<9935. 문자열 폭발>
골드4
https://www.acmicpc.net/problem/9935
'''

texts = list(input())
ex = list(input())
last = ex[-1]
length = len(ex)

stack = list()

for text in texts:
    stack.append(text)
    if text == last:
        if stack[(-1*length):] == ex:
            for _ in range(length):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))