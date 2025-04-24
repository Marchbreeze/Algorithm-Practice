'''
<12015. 가장 긴 증가하는 부분 수열 2>
골드2
https://www.acmicpc.net/problem/12015
'''

n = int(input())
array = list(map(int, input().split()))
lis = [array[0]]

def find_index(target):
    start = 0
    end = len(lis) - 1
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1,n):
    if array[i] > lis[-1]:
        lis.append(array[i])
    else:
        idx = find_index(array[i])
        lis[idx] = array[i]

print(len(lis))