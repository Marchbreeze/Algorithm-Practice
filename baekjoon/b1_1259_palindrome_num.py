'''
<1259. 팰린드롬수>
브론즈1
https://www.acmicpc.net/problem/1259
'''

while True:
    n = input().strip()
    if n == '0':
        break
    if n == n[::-1]:
        print("yes")
    else:
        print("no")