
# 이진 탐색 소스코드
def binary_search(array, target, start, end):
	if (start > end) :
		return None
	mid = (start + end) // 2
	if (array[mid] == target) :
		return mid
	elif (array[mid] > target) :
		return binary_search(array, target, start, mid-1)
	else :
		return binary_search(array, target, mid+1, end)
		
# 상점 입력값 입력
n = int(input())
storeList = list(map(int, input().split()))
storeList.sort()

# 고객 입력값 입력
m = int(input())
buyList = list(map(int, input().split()))

# 고객의 부품 번호를 하나씩 확인
for i in buyList :
	result = binary_search(storeList, i, 0, n-1)
	if (result != None) :
		print('yes', end='')
	else :
		print('no', end='')
