'''
<2309. 일곱 난쟁이>
브론즈1
https://www.acmicpc.net/problem/2309
'''

# 9명 중 합이 100이 되는 7명 찾기

# 키 입력
height = []
for _ in range(9):
    height.append(int(input()))

# 총합 찾기
none = sum(height) - 100

# 오름차순 정렬
height.sort()

# 두개 비교하며 합 none 찾기
isFound = False
for i in range(9):
    for j in range(i,9):
        if (height[i] + height[j] == none):
            height.pop(i)
            height.pop(j-1)
            isFound = True
            break
    if (isFound is True):
        break

# 결과 출력
for i in range(7):
    print(height[i])