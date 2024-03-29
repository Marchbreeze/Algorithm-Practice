'''
<5073. 삼각형과 세 변>
브론즈3
https://www.acmicpc.net/problem/5073
'''

# 세 변 길이 입력
input_list = []
while True:
    array = list(map(int, input().split()))
    if (array[0]== 0 and array[1] == 0 and array[2] == 0):
        break
    else:
        input_list.append(array)

# 삼각형 종류 확인
def check_triangle(tri):
    tri.sort(reverse=True)
    if (tri[0] >= tri[1] + tri[2]):
        print("Invalid")
    elif (tri[0] == tri[1] and tri[0] == tri[2] and tri[1] == tri[2]):
        print("Equilateral")
    elif (tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]):
        print("Isosceles")
    else:
        print("Scalene")

# 입력된 모든 삼각형 확인
for tri in input_list:
    check_triangle(tri)
    