'''
<02. 곱하기 혹은 더하기>
각 자리가 0~9의 숫자로 이루어진 문자열 S가 있다.
숫자 사이에 X 혹은 +를 넣어 가장 큰 수를 만들고자 한다.
모든 연산은 왼쪽에서부터 이루어진다.
(1 <= S길이 <= 20)
'''

# 숫자 입력받기
number = input()

# 연산 결과 초기화 후 첫 글자 넣기
result = int(number[0])

for i in range(1, len(number)):
    num = int(number[i])
    if (num <= 1 or result <= 1):
        result += num
    else:
        result *= num

print(result)