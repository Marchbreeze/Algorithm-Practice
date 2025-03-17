'''
<1972. 놀라운 문자열>
실버3
https://www.acmicpc.net/problem/1972
'''

while True:
    text = input()
    if (text == "*"):
        break
    n = len(text)
    for i in range(2, n+1):
        isExit = False
        _set = set()
        for j in range(n-i+1):
            d = text[j] + text[j+i-1]
            if (d in _set):
                print(text, "is NOT surprising.")
                isExit = True
                break
            else:
                _set.add(d)
        if (isExit is True):
            break
    else:
        print(text, "is surprising.")