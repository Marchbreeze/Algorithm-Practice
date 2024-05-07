'''
<1541. 잃어버린 괄호>
실버2
https://www.acmicpc.net/problem/1541
'''

# eval(expression)
# 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
# ex. eval("math.pi * pow(5, 2)")
# ex. x = 10 \ eval("x * 5")
# ex. eval("x > 5 and x < 9")

# 시도 1. eval 활용 -> 숫자 앞 0에 의해 실패
# - 기준으로 분리
'''
word = input().strip().split('-')

# - 기준으로 괄호 역할 적용
result = eval(word[0])
for i in range(len(word)-1):
    result -= eval(word[i+1])

print(result)
'''

# 시도 2. + 기준으로 다시 분리
# - 기준으로 분리
word = input().strip().split('-')

# 숫자 앞에 0 삭제
total = []
for i in range(len(word)):
    temp = word[i].split('+')
    count = 0
    for j in range(len(temp)):
        count += int(temp[j])
    total.append(count)

# - 기준으로 괄호 역할 적용
result = total[0]
for i in range(len(total)-1):
    result -= total[i+1]

print(result)