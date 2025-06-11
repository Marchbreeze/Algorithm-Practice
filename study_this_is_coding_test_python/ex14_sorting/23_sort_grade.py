'''
< 23. 국영수 >
학생 N명의 이름, 국어, 영어, 수학 점수가 주어질 때
1. 국어 점수가 감소하는 순서로
2. 1 동일시 영어 점수가 증가하는 순서로
3. 2 동일시 수학 점수가 감소하는 순서로
4. 3 동일시 이름이 사전 순으로 증가하는 순서로 정렬하시오.
(1 <= N <= 100,000, 1 <= 점수 <= 100)
'''

# 학생 수 입력
n = int(input())

# 점수 입력
array = []
for i in range(n):
    name, k, y, s = input().split()
    array.append((name, int(k), int(y), int(s)))

array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in array:
    print(student[0])