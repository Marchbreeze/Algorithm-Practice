def solution(id_list, report, k):
    
    # 신고-피신고 2차원 리스트 생성
    n = len(id_list)
    array = [[0] * n for _ in range(n)]
    
    # id 딕셔너리 설정
    id_dict = dict()
    for i in range(n):
        id_dict[id_list[i]] = i
    
    # report 분리
    report_from = []
    report_to = []
    for i in range(len(report)):
        x, y = report[i].split()
        report_from.append(x)
        report_to.append(y)
    
    # 신고 여부 전환
    for i in range(len(report)):
        array[id_dict[report_from[i]]][id_dict[report_to[i]]] = 1
    
    # 제재 여부 확인
    for i in range(n):
        count = 0
        for j in range(n):
            if (array[j][i] == 1):
                count += 1
        if (count >= k):
            for j in range(n):
                if (array[j][i] == 1):
                    array[j][i] = 2

    # 신고 성공 여부 확인
    result = []
    for i in range(n):
        count = 0
        for j in range(n):
            if (array[i][j] == 2):
                count += 1 
        result.append(count)
    
    return result