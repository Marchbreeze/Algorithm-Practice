'''
< 10. 자물쇠와 열쇠 >
잠겨있는 NxN 크기의 자물쇠는 홈이 파여 있고, MxM 크기의 열쇠 또한 홈과 돌기 부분이 있다.
(3 <= M <= N <= 20, 0은 홈 부분, 1은 돌기 부분)
열쇠는 회전과 이동이 가능하며, 열쇠의 돌기 부분을 자물쇠의 홈 부분에 맞추면 자물쇠가 열린다.
자물쇠 영역 내부에서는 모든 홈에 정확히 일치해야하며, 열쇠의 돌기와 자물쇠의 돌기가 만날 수 없다.

답안 아이디어 :
1. 자물쇠의 주위를 0으로 채워 3N x 3N 크기로 만든다.
2. 열쇠를 모든 곳에, 4방향으로 돌리며 모두 더해본다.
3. 자물쇠 부분이 모두 1로만 채워지면 열린다.
'''

# 2차원 리스트 90도 회전 함수
def rotate_matrix(mat):
	n = len(mat)
	m = len(mat[0])
	result = ([0] * n for _ in range(m))
	for i in range(n):
		for j in range(m):
			result[j][n-i-1] = mat[i][j]
	return result

# 자물쇠 확인 구현
def check(new_lock):
	lock_length = len(new_lock) // 3
	for i in range(lock_length, lock_length*2):
		for j in range(lock_length, lock_length*2):
		    if (new_lock[i][j] != 1):
			    return False
	return True

# 문제 풀이 구현
def solution(key, lock):
	n = len(lock)
	m = len(key)
	
	# 자물쇠 크기 변환
	new_lock = [[0] * (n * 3) for _ in range(n * 3)]
	for i in range(n):
		for j in range(n):
			new_lock[i+n][j+n] = lock[i][j]
	
    # 4가지 방향에 대해서 확인
	for rotation in range(4):
		key = rotate_matrix(key)
		for x in range(n*2):
			for y in range(n*2):
				array = new_lock
				for i in range(n):
					for j in range(m):
						array[x+i][y+j] += key[i][j]
				if check(array):
					return True

	return False