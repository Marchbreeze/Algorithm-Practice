'''
<10799. 쇠막대기>
실버2
https://www.acmicpc.net/problem/10799
'''

ir = input()
stack = []
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else :
        if ir[i-1]=="(":
            stack.pop()
            cnt+=len(stack)
            
        else :
            stack.pop()
            cnt+=1 
print(cnt)