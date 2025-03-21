'''
<1904. 01타일>
실버3
https://www.acmicpc.net/problem/1904
'''

# 타일 종류 : 00, 1
# 타일 N개일 때 만들 수 있는 모든 가짓수 도출

# 1개 : 1
# 2개 : 11, 00
# 3개 : 111, 100, 001 = 2개 뒤에 1, 1개 뒤에 00
# 4개 : 1111, 1100, 1001, 0011, 0000 = 3개 뒤에 1, 2개 뒤에 00

n = int(input())
table = [0,1,2]

for i in range(3,n+1):
    table.append((table[i-1] + table[i-2]) % 15746)

print(table[n])
