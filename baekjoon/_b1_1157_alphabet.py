'''
<1157. 단어 공부>
브론즈1
https://www.acmicpc.net/problem/1157
'''

# 단어 카운트용 딕셔너리 생성
alpha_list = [chr(i) for i in range(ord('a'), ord('z')+1)] 
alpha_dict = dict()
for letter in alpha_list:
    alpha_dict[letter] = 0

# 소문자 영어 입력
letter = input().upper()

for i in range(len(letter)):
    alpha_dict[letter[i]] += 1

# 제일 큰 카운트 찾기
max_value = max(alpha_dict.values())
max_keys = [key for key, value in alpha_dict.items() if value == max_value]
if (len(max_keys) == 1):
    print(max_keys[0])
else:
    print("?")