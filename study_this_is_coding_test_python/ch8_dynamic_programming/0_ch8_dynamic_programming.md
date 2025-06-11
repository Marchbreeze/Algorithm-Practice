---

## 다이나믹 프로그래밍(DP)

- 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘
- 메모리 공간을 약간 더 사용해서 연산 속도를 비약적으로 증가시켜줌
- 사용 조건 :
    1. 큰 문제를 작은 문제로 나눌 수 있다.
    2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
    

### (1) 탑다운 방식- 메모이제이션 (캐싱)

- `재귀함수` 활용한 DP
- 한 번 구한 결과를 메모리 공간에 메모해두고, 같은 식을 호출 시 메모해둔 결과를 그대로 가져오게 됨
- 단, 시스템 상 재귀함수의 스택 크기가 제한될 위험 존재 (일반적으로 5000번)
- ex) 피보나치 수열
    - 재귀함수로 구현하는 경우, 100번째를 구하기 위해 1~99번쨰 연산을 모두 반복해서 수행해야 함
    - 한 번 구한 정보를 리스트에 저장한 후 활용한다면 반복 수행을 막을 수 있음
    
    ```python
    # 메모 리스트 초기화
    memo = [0] * 100
    
    # 피보나치 함수를 재귀함수로 구현 (탑다운 DP)
    def fibo(x):
    		if (x==1 or x==2) :
    				return 1
    		# 이미 계산한 적 있는 문제라면 메모에서 값 가져옴
    		if (memo[x] != 0) :
    				return memo[x]
    		# 처음 계산이라면 점화식에 따라 결과 반환
    		memo[x] = fibo(x-1) + fibo(x-2)
    		return memo[x]
    
    print(fibo(99))
    ```
    

### (2) 바텀업 방식 - DP Table

- 재귀함수 대신 `반복문` 활용한 DP
- 메모 대신 DP Table 이라고 불림
- 탑다운의 경우, 사실상 호출될 필요가 없음에도 메모리 상 적재되는 과정이 필요해 오버헤드가 발생할 수 있음
- ex) 피보나치 수열
    
    ```python
    # 메모 리스트 초기화
    dpTable = [0] * 100
    dpTable[1] = 1
    dpTable[2] = 1
    
    for i in range(3, 100):
    		dpTable[i] = dpTable[i-1] + dpTable[i-2]
    
    print(memo(99))
    ```
    

## 2. 연산을 조합해 1 만들기

<aside>
❔ 정수 X에 사용할 수 있는 연산은 4가지이다.

1. X가 5로 나누어 떨어지면, 5로 나눈다.
2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
3. X가 2로 나누어 떨어지면, 2로 나눈다.
4. X에서 1을 뺀다.

연산 4개들을 적절히 사용해서 1을 만들려고 할 때, 사용 횟수의 최솟값을 구하시오.
(1 ≤ X ≤ 30,000)

</aside>

- 풀이
    - 한 숫자에서 1로 가는 방법은 결국에는 항상 동일함
    - 작은 숫자로 줄인 후, 기존에 진행했던 연산을 진행 → DP 활용히는 것이 좋음
        
        ![2024-03-13_18-37-58.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/e1a49ee8-4b59-45b5-a27c-2acda34eb74a/2024-03-13_18-37-58.jpg)
        
    - 바텀-업 방식으로 진행
        
        ```python
        # 정수 입력받기
        x = int(input())
        
        # DP Table 초기화하기
        dpTable = [0] * 30001
        
        # 바텀업 DP 진행
        for i in range(2, x+1) :
            # 1을 빼기
            dpTable[i] = dpTable[i-1] + 1
            # 2로 나누기
            if (i % 2 == 0) :
                dpTable[i] = min(dpTable[i], dpTable[i//2] + 1)
            # 3으로 나누기
            if (i % 3 == 0) :
                dpTable[i] = min(dpTable[i], dpTable[i//3] + 1)
            # 5로 나누기
            if (i % 5 == 0) :
                dpTable[i] = min(dpTable[i], dpTable[i//5] + 1)
        
        print(dpTable[x])
        ```
        
    
    ## 3. 한 칸 이상 떨어진 식량 창고 선택
    
    <aside>
    ❔ 식량창고 N개가 일직선으로 이어져 있으며, 각 K개의 식량을 가지고 있다.
    (3 ≤ N ≤ 100, 0 ≤ K ≤ 1,000)
    
    서로 인접한 식량창고에서는 식량을 얻을 수 없으며, 최소한 한 칸 떨어진 식량창고들을 선택해야 한다.
    
    얻을 수 있는 식량의 최댓값을 구하시오.
    
    </aside>
    
    ![2024-03-13_18-53-40.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/22a0aee4-25c0-4670-90d9-9524efcfe83e/2024-03-13_18-53-40.jpg)
    
    - 풀이
        - 작은 단위로 쪼개보기
        - 1개 전, 2개 전 경우만 고려하면 됨 (3개부터는 아무런 상관 없이 가능)
            
            ![2024-03-13_18-54-28.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/9b699f41-6cf7-4b9a-996f-53aa1a526a1f/2024-03-13_18-54-28.jpg)
            
        - 점화식 활용한 바텀업
            
            ```python
            # 정수, 식량 리스트 입력받기
            x = int(input())
            array = list(map(int, input().split()))
            
            # DP Table 초기화하기
            dpTable = [0] * 100
            
            # 점화식을 위한 0, 1번째 값 설정
            dpTable[0] = array[0]
            dpTable[1] = max(array[0], array[1])
            
            # 바텀업 DP 진행
            for i in range(2, x) :
                dpTable[i] = max(dpTable[i-1], dpTable[i-2] + array[i])
            
            print(dpTable[x-1])
            ```
            
    
    ## 4. 바닥 타일 경우의 수 구하기
    
    <aside>
    ❔ 가로 N, 세로 2인 직사각형 형태의 바닥이 있다.
    (1 ≤ N ≤ 1,000)
    
    3개 종류의 바닥 덮개 (1x2, 2x1, 1x2)로 바닥을 채우고자 한다.
    
    바닥을 채우는 모든 경우의 수는 ?
    
    </aside>
    
    - 풀이
        - 맨 마지막 경우들만 고려해서 점화식 생각하기
            
            ![2024-03-13_19-12-53.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/9f51f5f4-0bd2-4425-994d-e611c065ac47/2024-03-13_19-12-53.jpg)
            
        - 점화식 :
            
            ![2024-03-13_19-14-03.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/37ba63a0-ba14-4339-a5da-e081a10ff076/2024-03-13_19-14-03.jpg)
            
        - 바텀업 :
            
            ```python
            # 정수 입력받기
            n = int(input())
            
            # DP Table 초기화하기
            dpTable = [0] * 100
            
            # 점화식을 위한 1, 2번째 값 설정
            dpTable[1] = 1
            dpTable[2] = 3
            
            # 바텀업 DP 진행
            for i in range(3, n+1) :
                dpTable[i] = dpTable[i-1] + dpTable[i-2] * 2
            
            print(dpTable[n])
            ```
            
    
    ## 5. 최소한의 화폐로 구성하기
    
    <aside>
    ❔ N개 종류의 화폐를 가치의 합이 M원이 되도록 하는 최소한의 화폐 개수를 구하시오.
    (1 ≤ N ≤ 100, 1 ≤ M ≤ 10,000)
    
    단, 불가능한 경우 -1을 출력하시오.
    
    </aside>
    
    - 풀이
        - 거스름돈 문제와 비슷하면서도, 큰 단위가 작은 단위의 배수가 될 수 있기 때문에 DP를 활용해야 함
        - 점화식 :
            
            ![2024-03-14_04-21-21.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/c1bb770d-7cdd-48b5-9cc2-478b3bf85a25/2024-03-14_04-21-21.jpg)
            
            - 금액 i를 만들 수 있는 최소한의 화폐 개수 : ai
            - 화폐의 단위 : k
        - 예시 :
            - N=3, K=7, 단위: 2,3,5 일떄
            
            ![2024-03-14_04-22-32.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/90a01b84-683b-4250-abd8-71195b60a490/2024-03-14_04-22-32.jpg)
            
            ![2024-03-14_04-22-53.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/9621c775-e8da-4b3a-976c-fe0900e259de/2024-03-14_04-22-53.jpg)
            
        - 구현 :
            
            ```python
            # 정수 입력받기
            n,m = map(int, input().split())
            
            # 화폐 단위 입력받기
            array = []
            for i in range(n):
                array.append(int(input()))
            
            # DP Table 설정
            dpTable = [10001] * (m+1)
            dpTable[0] = 0
            
            # 바텀업 진행
            for i in range(n):
                for j in range(array[i], m+1):
                    dpTable[j] = min(dpTable[j], dpTable[j-array[i]] + 1)
            
            # 결과
            if (dpTable[m] == 10001):
                print(-1)
            else:
                print(dpTable[m])
            ```