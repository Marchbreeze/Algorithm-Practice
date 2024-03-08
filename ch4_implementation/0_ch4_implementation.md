---

## 아이디어를 코드로 바꾸는 구현

- 문제 풀이 방법을 코드로 작성하기 까다로운 문제
- `완전 탐색` : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
- `시뮬레이션` : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행해야 하는 해결 방법

### ex) 시뮬레이션 - 상하좌우

<aside>
❔ N x N 크기의 공간이 가장 왼쪽 위 (1,1) 부터 오른쪽 아래 (N,N) 의 좌표로 구현되어 있을 때,

여행 계획서에는 L(왼쪽 한칸), R, U, D의 지침이 있으며, 공간을 벗어나려는 움직임은 무시된다.

N x N 크기의 공간에서 (1,1) 좌표부터 계획서에 의해 도착할 최종 좌표를 구하시오. 
(1 ≤ N, 횟수 ≤ 100)

</aside>

- 풀이
    - 일반적으로 `방향을 설정하는 문제`는 `dx, dy`라는 리스트를 따로 만들어 방향을 정하는 것이 효과적
        
        → 반복문을 활용하여 모든 방향을 차례대로 확인할 수 있음
        
    
    ```python
    # 좌표 크기 입력받기
    n = int(input())
    
    # 계획서 입력받기
    x, y = 1, 1
    plans = input().split()
    
    # 이동 방향 설정하기
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ["L", "R", "U", "D"]
    
    # 공간을 넘지 않는 경우 이동하기
    for plan in plans :
        for i in range(len(move_types)) :
            if (plan == move_types[i]) :
                nx = x + dx[i]
                ny = y + dy[i]
        if (1 <= nx <= n and 1 <= ny <= n) :
            x, y = nx, ny
    
    print(x, y)
    ```
    

### ex) 완전 탐색 - 3 포함 시각

<aside>
❔ 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서

3이 하나라도 포함되는 모든 경우의 수를 구하시오

</aside>

- 풀이
    - `완전 탐색` : 모든 수를 검사
    - 일반적으로 비효율적인 시간 복잡도를 가지고 있으므로, 전체 데이터가 `100만 개 이하일 때` 활용
    - 삼중 반복문 활용
        
        ```python
        # 시 입력받기
        n = int(input())
        
        # 모두 탐색하기
        count = 0
        for i in range(n+1) :
        		for j in range(60) :
        				for k in range(60) :
        						if '3' in str(i) + str(j) + str(k) :
        								count += 1
        
        print(count)
        ```
        
    

## 1. 체스 나이트 이동 경우의 수

<aside>
❔ 8 x 8 좌표에서의 나이트는 다음과 같이 이동한다.

1. 수평으로 두 칸 이동 후 수직으로 한 칸 이동
2. 수직으로 한 칸 이동 후 수평으로 한 칸 이동

나이트의 위치가 주어졌을 때, 8가지 중 이동할 수 있는 경우의 수를 구하시오.

</aside>

- 풀이
    
    ```python
    # 나이트의 위치 입력받기 - a1
    start = input()
    row = int(start[1])
    column = int(ord(start[0])) - int(ord('a')) + 1
    
    # 나이트 이동 방향 정의
    steps = [(-2,-1), (-1,-2), (-2,1), (-1,2), (2,-1), (1,-2), (2,1), (1,2)]
    
    # 8가지 경우에 대해서 가능 여부 확인
    count = 0
    for step in steps :
        new_row = row + step[0]
        new_column = column + step[1]
        if (1 <= new_row <= 8 and 1 <= new_column <= 8) :
            count += 1
    
    print(count)
    
    ```
    

## 2. 게임 캐릭터 움직이는 시스템 설계

<aside>
❔ 캐릭터는 N x M 크기의 직사각형에서 상하좌우로 움직인다. (3 ≤ N, M ≤ 50)

맵의 각 칸은 (A, B)로 나타낼 수 있고, 
A = 북쪽에서 떨어진 칸 수, B = 서쪽에서 떨어진 칸 수이다.

각 칸은 육지 or 바다로 구성되어 있다.
바다로 된 공간에는 갈 수 없으며, 맵의 외곽은 항상 바다이며, 시작하는 칸은 항상 육지이다.
(0: 육지, 1: 바다)

캐릭터는 동서남북 중 한 곳을 바라본다.
(0: 북쪽, 1:동쪽, 2: 남쪽, 3:서쪽)

움직임의 메뉴얼은 다음과 같다.
1. 현재 위치, 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
2-1. 왼쪽 방향에 가보지 않은 칸이 존재한다면, 왼쪽으로 회전 후 한 칸을 전진한다.
2-2. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽으로 회전만 진행한다.
3. 네 방향 모두 가본 칸이거나 바다로 된 칸인 경우, 바라보는 방향을 유지한 채 한 칸 뒤로 가고 1단계로 돌아간다. 뒤쪽 방향이 바다인 경우는 움직임을 멈춘다.

메뉴얼에 따라 캐릭터를 이동시킨 후, 방문한 칸의 개수를 출력하시오.

</aside>

![2024-03-09_00-26-02.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/bebb681b-2fa5-4f41-adb3-00b02322eb7c/2024-03-09_00-26-02.jpg)

- 풀이
    - 2차원 배열 0으로 채우기
        
        `visit = [[0] * m for _ in range(n)]`
        
    - 2차원 배열 input으로 받기
        
        `for i in range(n) : 
            gameMap.append(list(map(int, input().split())))`
        
    
    ```python
    
    # 맵 크기 입력받기
    n, m = map(int, input().split())
    
    # 캐릭터 위치, 방향 입력받기
    x, y, direction = map(int, input().split())
    
    # 전체 맵 정보 입력받기
    gameMap = []
    for i in range(n) :
        gameMap.append(list(map(int, input().split())))
    
    # 동서남북 방향 정의
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 방문 위치 저장용 맵 생성
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1
    
    # 왼쪽으로 회전 함수 정의
    def turn_left() :
        global direction
        if (direction == 0) :
            direction = 3
        else :
            direction -= 1
    
    # 시뮬레이션
    count = 1
    turn_count = 0
    while True :
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        if (visit[nx][ny] == 0 and gameMap[nx][ny] == 0) :
            visit[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_count = 0
            continue
        else :
            turn_count += 1
            if (turn_count == 4) :
                nx = x - dx[direction]
                ny = y - dy[direction]      
                if (gameMap[nx][ny] == 0) :
                    x = nx
                    y = ny
                    turn_count = 0
                else :
                    break
    
    print(count)
    
    ```