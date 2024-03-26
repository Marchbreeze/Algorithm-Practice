def solution(today, terms, privacies):
    
    # terms 딕셔너리 형태로 변환
    dict = {}
    for item in terms:
        key, value = item.split()  
        dict[key] = int(value)  
        
    # 오늘 날짜 리스트화
    today_list = today.split('.')
    
    # 개인정보 리스트화
    privacy_list = []
    privacy_type = []
    for i in range(len(privacies)):
        date, type = privacies[i].split()
        y, m, d = date.split('.')
        privacy_type.append(type)
        privacy_list.append([int(y), int(m), int(d)])

    # 개인정보에 조건 넣어 비교
    result = []
    for i in range(len(privacy_list)):
        add_date(privacy_list[i], dict[privacy_type[i]])
        if not (is_date_left(today_list, privacy_list[i])):
            result.append(i+1)
    return result
        
        
# 날짜 비교 함수
def is_date_left(today, date):
    if (int(today[0]) > date[0]):
        return False
    elif (int(today[0]) < date[0]):
        return True
    else:
        if (int(today[1]) > date[1]):
            return False
        elif (int(today[1]) < date[1]):
            return True
        else:
            if (int(today[2]) >= date[2]):
                return False
            else:
                return True

# 날짜 추가 함수
def add_date(date, term):
    date[1] += term
    while (date[1] > 12):
        date[0] += 1
        date[1] -= 12