'''
<9506. 약수들의 합>
브론즈1
https://www.acmicpc.net/problem/9506
'''

while True:
    num = int(input())
    if (num == -1):
        break
    array = []
    for i in range(1, num):
        if (num % i == 0):
            array.append(i)
    sum = 0
    for j in array:
        sum += j
    if (num == sum):
        ans = " + ".join(map(str, array))
        print(num,"=", ans)
    else:
        print(num, "is NOT perfect.")