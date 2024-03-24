def solution(survey, choices):

		# 지표 (RT, CF, JM, AN) - 검색 위해 dict 활용
		my_type = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
		
		# 유형 결과 계산
		for i in range(len(survey)):
		    my_type[survey[i][0]] += 4 - choices[i]
		
		# 각 지표끼리 비교 진행 - dict을 인덱스 활용 위해 리스트로 전환
		my_list = list(my_type.items())
		result = []
		for i in range(4):
		    if (my_list[i*2][1] < my_list[i*2+1][1]):
		        result.append(my_list[i*2+1][0])
		    else:
		        result.append(my_list[i*2][0])
		
		# 결과값 문자열로 변환
		answer = ''.join(result)
		return answer