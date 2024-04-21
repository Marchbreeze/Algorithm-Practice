'''
<10988. 팰린드롬인지 확인하기>
브론즈3
https://www.acmicpc.net/problem/10988
'''

# 단어 앞뒤 비교
def check_palindrome(word):
    n = len(word) // 2
    for i in range(n):
        if (word[i] != word[-i-1]):
            return 0
    return 1

# 단어 입력
w = input().strip()
print(check_palindrome(w))