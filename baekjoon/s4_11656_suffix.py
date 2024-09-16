'''
<11656. 접미사 배열>
실버4
https://www.acmicpc.net/problem/11656
'''

# baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지
# 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon
# 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성

# 문자열 입력
s = input()
array = []

# 리스트에 접미사 추가
for i in range(len(s)):
    array.append(s[i:len(s)])

# 리스트 정렬 후 출력
array.sort()
for j in array:
    print(j)