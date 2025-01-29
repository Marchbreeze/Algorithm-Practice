'''
<4153. 직각삼각형>
브론즈3
https://www.acmicpc.net/problem/4153
'''

while True :
    array = list(map(int, input().split()))
    array.sort(reverse=True)
    if(array[0] == 0) :
        break
    if(array[0]**2 == array[1]**2 + array[2]**2):
        print("right")
    else:
        print("wrong")