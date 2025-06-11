'''
< 09. 문자열 압축 >
문자열을 1개 이상의 단위로 잘라서 압축해, 더 짧은 문자열로 표현하고자 한다.
ababcdcdababcdcd = 2ab2cd2ab2cd or 2ababcdcd
문자열 S를 1개 이상 단위로 문자열을 잘라 압축하여 표현할 때 가장 짧은 것의 길이를 구하시오.
(1 <= S의 길이 <= 1,000)
'''

# 문자열 입력
s = input()

# 1개 단위부터 S의 길이까지 모두 단위로 잘라보기
result = len(s)

for unit in range(1, len(s)):
    temp = ""
    length = len(s)
    for i in range(0, len(s), unit):
        str = s[i:i+unit]
        if (str == temp):
            length -= unit - 1
        else:
            temp = str
    result = min(result, length)

# 결과 출력
print(result)