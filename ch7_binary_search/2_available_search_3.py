
# 상점 입력값 입력
n = int(input())
storeList = set(map(int, input().split()))

# 고객 입력값 입력
m = int(input())
buyList = list(map(int, input().split()))

# 고객의 부품 번호를 하나씩 확인
for i in buyList :
	if (i in storeList) :
		print('yes', end='')
	else :
		print('no', end='')