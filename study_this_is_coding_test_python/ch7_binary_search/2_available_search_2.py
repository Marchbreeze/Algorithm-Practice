
# 가게 부품 입력받기
n = int(input())

# 가게의 전체 부품 리스트에 입력받기
array = [0] * 100001
for i in input().split():
    array[int(i)] = 1

# 고객의 부품 입력받기
m = int(input())
buyList = list(map(int, input().split()))

# 고객의 부품 하나씩 확인하기
for i in buyList :
    if array[i] == 1:
       print('yes', end='')
    else :
        print('no', end='')