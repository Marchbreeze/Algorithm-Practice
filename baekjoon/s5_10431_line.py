'''
< 10431. 줄 세우기 >
실버5
https://www.acmicpc.net/problem/10431
'''

# 키 순서로 번호 부여
# 1. 아무나 한명 뽑아 맨 팡세 세움
# 2. 학생이 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거침
# 2-1. 자기 앞에 키가 큰 사람이 없다면 그자리에 서고 끝암
# 2-2. 자기 앞에 키가 큰 사람이 있다면 그 중 가장 앞에 이있는 학생 앞에 서고, 모두 한발씩 뒤로 감

# 테스트 케이스 개수 입력
test = int(input())

# 테스트마다 진행
for _ in range(test):

    # 테스트 케이스 입력받기
    array_input = list(map(int, input().split()))
    case, array = array_input[0], array_input[1:]
    
    # 삽입 정렬 진행
    count = 0
    sort_array = []
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if (array[j] < array[j - 1]):
                array[j], array[j - 1] = array[j - 1], array[j]
                count += 1
            else :
                break
    
    # 출력하기
    print(case, count)