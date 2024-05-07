'''
<1439. 뒤집기>
실버5
https://www.acmicpc.net/problem/1539
'''

import math

word = input().strip()
count = 0
for i in range(len(word)-1):
    if (word[i:i+2] == '01' or word[i:i+2] == '10'):
        count += 1

print(math.ceil(count/2))