'''
<4949. 균형잡힌 세상>
실버4
https://www.acmicpc.net/problem/4949
'''

while True:
    text = input()
    if text == ".":
        break
    stack = []
    answer = "yes"
    for char in text:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                answer = "no"
                continue
            prev = stack.pop()
            if prev != "(":
                answer = "no"
                continue
        elif char == "]":
            if len(stack) == 0:
                answer = "no"
                continue
            prev = stack.pop()
            if prev != "[":
                answer = "no"
                continue
    print(answer)