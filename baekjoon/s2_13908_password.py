'''
<13908. 비밀번호>
실버2
https://www.acmicpc.net/problem/13908
'''

# 비밀번호의 길이와 선견지명으로 알게된 비밀번호의 일부 숫자가 주어질 때, 모든 가능한 비밀번호의 개수를 출력하는 프로그램을 작성

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
m_list = []
if (m != 0):
    m_list = list(map(int, input().split()))

stack = [([], 0)]
count = 0

while stack:
    nums, digit = stack.pop()
    if (digit == n):
        picked = set()
        for num in nums:
            if (num in m_list):
                picked.add(num)
        if (len(picked) == m):
            count += 1
    else:
        for i in range(10):
            new_nums = nums.copy()
            new_nums.append(i)
            stack.append((new_nums, digit + 1))

print(count)