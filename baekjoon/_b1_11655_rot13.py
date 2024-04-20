'''
<11655. ROT13>
브론즈1
https://www.acmicpc.net/problem/11655
'''

'''
https://black-hair.tistory.com/162
https://youjin86.tistory.com/45
'''


# ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
# 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다

# 문자 입력
word = input()

# 코드 변환
answer = ''
for x in word:
    if ('a'<=x and x<='z'):
        x = ord(x)+13
        if (x > 122):
            x -= 26
        answer += chr(x)
    elif ('A'<=x and x<='Z'):
        x = ord(x)+13
        if (x > 90):
            x -= 26
        answer += chr(x)
    else:
        answer += x

print(answer)