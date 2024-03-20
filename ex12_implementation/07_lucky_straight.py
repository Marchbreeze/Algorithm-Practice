'''
< 07. 럭키 스트레이트 >
현재 캐릭터의 점수를 N이라고 할 때,
자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분과 오른쪽 부분의 각 자릿수 합이 동일한 상황이면
기술을 사용할 수 있다. 사용 가능 여부를 알려주는 프로그램을 만드시오.
(10 <= N <= 99,999,999, N의 자릿수는 항상 짝수)
'''

# N 입력
n = input()

# 비교할 합 처리
left_sum = 0
right_sum = 0

# 왼쪽 처리
left = n[: len(n)//2]
for i in left:
    left_sum += int(i)

# 오른쪽 처리
right = n[len(n)//2 :]
for i in right:
    right_sum += int(i)

# 결과값 출력
if (left_sum == right_sum):
    print("LUCKY")
else:
    print("READY")

'''
답지 :
lef_sum & right_sum 대신
sum 하나로 하고, left일때는 +, right일떄는 -로 최종 값이 0인지 아닌지 판단함
'''