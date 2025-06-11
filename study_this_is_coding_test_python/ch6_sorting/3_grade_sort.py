
# 학생 수 입력받기
n = int(input())

# N명의 학생을 입력받고 리스트에 저장하기
array = []
for i in range(n) :
    input_data = input().split()
    array.append(input_data[0],int(input_data[1]))

# key를 활용해 정수 값을 기준으로 정렬하기
array = sorted(array, key=lambda student: student[1])

# 정렬된 순서로 출력
for student in array:
    print(student[0], end='')
