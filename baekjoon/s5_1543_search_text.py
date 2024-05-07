'''
<1543. 문자 검색>
실버5
https://www.acmicpc.net/problem/1543
'''

sentence = input().strip()
n = len(sentence)
word = input().strip()
m = len(word)

isUsed = [False] * n
count = 0
for i in range(n-m+1):
    if (sentence[i:i+m] == word and isUsed[i] is False):
        count += 1
        for j in range(m):
            isUsed[i+j] = True

print(count)