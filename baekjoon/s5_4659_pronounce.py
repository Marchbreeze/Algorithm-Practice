'''
<4659. 비밀번호 발음하기>
실버5
https://www.acmicpc.net/problem/4659
'''

vowels = set('aeiou')

# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
def not_contains_vowel(word):
    for char in word:
        if char in vowels:
            return False
    return True

# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
def three_in_row(word):
    for i in range(len(word)-2):
        if (word[i] in vowels and word[i+1] in vowels and word[i+2] in vowels):
            return True
        if (word[i] not in vowels and word[i+1] not in vowels and word[i+2] not in vowels):
            return True
    return False

# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
def two_in_row(word):
    for i in range(len(word)-1):
        if (word[i] == word[i+1] and word[i] != 'e' and word[i] != 'o'):
            return True 
    return False

while True:
    # end 나올떄까지 반복
    word = input().strip()
    if (word == 'end'):
        break
    
    # 조건 하나씩 확인
    if (not_contains_vowel(word)):
        print(f"<{word}> is not acceptable.")
    elif (three_in_row(word)):
        print(f"<{word}> is not acceptable.")
    elif (two_in_row(word)):
        print(f"<{word}> is not acceptable.")
    else:
        print(f"<{word}> is acceptable.")