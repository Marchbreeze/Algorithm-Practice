'''
<11723. 집합>
실버5
https://www.acmicpc.net/problem/11723
'''
import sys

# 연산의 수 입력
m = int(sys.stdin.readline())

# 연산 진행
s = set()
for _ in range(m):
    array = sys.stdin.readline().strip().split()
    act = array[0]
    if (len(array) == 1):
        if (act == "all"):
            s = set(i for i in range(1,21)) 
        elif (act == "empty"):
            s = set()

    else:
        x = int(array[1])
        if (act == "add"):
            s.add(x)
        elif (act == "remove"):
            if (x in s):
                s.remove(x)
        elif (act == "check"):
            if (x in s):
                print(1)
            else:
                print(0)
        elif (act == "toggle"):
            if (x in s):
                s.remove(x)
            else:
                s.add(x)