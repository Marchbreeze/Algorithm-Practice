'''
<2562. 최댓값>
브론즈3
https://www.acmicpc.net/problem/2562
'''

num_list = []
for i in range(9):
    n = int(input())
    num_list.append(n)

max_num = sorted(num_list)[-1]

print(max_num)
print(num_list.index(max_num)+1)
