'''
<1874. 스택 수열>
실버2
https://www.acmicpc.net/problem/1874
'''

count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        temp = False
        break

if temp is False:
    print("NO")
else:
    for i in op:
        print(i)