---

## 그리디 알고리즘

- 탐욕 : 현재 상황에서 지금 당장 좋은 것만 고르는 방법 (나중의 영향 고려 X)
- 문제 조건 - `“가장 큰 순서대로”, “가장 작은 순서대로”`
- `/` : 나눗셈 결과,     `//` : 몫,     `%` : 나머지

### ex) 거스름돈

<aside>
❔ 거스름돈 500원, 100원, 50원, 10원이 무한히 있다고 가정하자.
거슬러줄 돈이 N원일 때, 최소 동전 개수를 구하라 (N은 항상 10의 배수)

</aside>

- 아이디어
    - `가장 큰 화폐 단위부터` 돈을 거슬러주기 - 500, 100, 50, 10 순
- 풀이
    
    ```python
    n = 1260
    count = 0
    
    # 큰 단위의 화폐부터 차례대로 확인
    coin_types = [500, 100, 50, 10]
    
    # 차례대로 거슬러줄 수 있는 동전 개수 세기
    for coin in coin_types :
    	count += n // coin
    	n %= coin
    
    print(count)
    ```
    
    - 시간 복잡도 : O(N)
    - 해결 가능한 이유 : 큰 단위가 항상 작은 단위의 배수여서 다른 해 도출 가능성 X
    - ex - 500, 400, 100이라면 → 800원은 (500+100+100+100) < (400+400)
        
        → 활용 전 정당성을 검토할 수 있어야 함
        

## 1. 큰 수의 법칙

<aside>
❔ 배열의 크기 N
숫자가 더해지는 횟수 M
배열의 특정 인덱스 번호가 연속해서 K번을 초과해서 더해질 수 없음

배열 내 N개의 숫자를 조건을 만족하여 M번 더하여 가장 큰 수를 만드시오

1<N<1000, 1<M<10000, 1<K<10000

</aside>

- 일반 풀이
    
    ```python
    # N,M,K 공백으로 구분해서 입력받기
    n, m, k = map(int, input().split())
    
    # N개의 수를 공백으로 구분해서 입력받기
    data = list(map(int, input().split()))
    
    # 입력값 중 1, 2번째로 큰 수만 골라내기
    data.sort()
    first = data[n-1]
    second = data[n-2]
    
    # K개씩 first 더하고, second 한번 더하고, M번 반복
    result = 0
    while True :
        for i in range(k) :
            result += first
            m -= 1
            if (m == 0) : 
                break
        result += second
        m -= 1
        if (m == 0) : 
            break
    
    print(result)
    ```
    

- 심화 풀이
    - `반복되는 수열에 대해서 파악하기`
        - M=8, K=3 → (6+6+6+5) + (6+6+6+5)
        - M=10, K=3 → (6+6+6+5) + (6+6+6+5) + (6+6)
    - M/(K+1) 개만큼 동일한 수열 반복 & 나머지만큼 first가 더해짐
        - first는 K*청크 개수 + 나머지 개수
        - second는 청크 개수
        - 만큼 더해짐
    
    ```python
    # N,M,K 공백으로 구분해서 입력받기
    n, m, k = map(int, input().split())
    
    # N개의 수를 공백으로 구분해서 입력받기
    data = list(map(int, input().split()))
    
    # 입력값 중 1, 2번째로 큰 수만 골라내기
    data.sort()
    first = data[n-1]
    second = data[n-2]
    
    # 반복되는 수열 계산
    chunk = m//(k+1)
    remainder = m%(k+1)
    
    # second 설정
    result = chunk * second
    
    # first 설정
    result += (chunk * k +  remainder) * first
    
    print(result)
    ```
    

## 2. 숫자 카드 게임

<aside>
❔ 숫자 카드들이 N x M 형태로 놓여 있음 (N: 행의 개수, M: 열의 개수)
1. 행을 선택
2. 행의 카드 중 가장 낮은 카드를 고름
행을 선택하는 경우들 중, 최종적으로 가장 높은 숫자의 카드를 출력하시오

1<N,M<100

</aside>

- 풀이
    
    ```python
    # N, M부터 입력받기
    n, m = map(int, input().split())
    
    # 한줄씩 입력받아서, 줄의 최소 수와 다른 줄의 값 비교
    result = 0
    for i in range(n) :
        data = list(map(int, input().split()))
        min_value = min(data)
        result = max(result, min_value)
    
    print(result)
    ```
    

## 3. 1이 될 때까지

<aside>
❔ 숫자를 1을 만들 때까지 다음 연산 중 하나를 반복적으로 수행
1. N에서 1을 뺀다.
2. N을 K로 나눈다 (나누어 떨어지는 경우)

연산을 수행하는 최소 횟수를 구하시오

1 < K ≤ N < 100,000

</aside>

- 풀이
    - 나누기가 빼기보다 더 숫자를 많이 줄여줌
        
        → 나누기 우선, 못 나누는 경우 나눌 수 있을때까지(배수일때까지) 1씩 빼기
        
        ```python
        # N,K 입력받기
        n, k = map(int, input().split())
        result = 0
        
        # 남은 N이 K 이상인 경우 계속 나누기
        while (n >= k) :
            if (n % k == 0) :
                n //= k
            else : 
                n -= 1
            result += 1
        
        # 모두 나눈 후 1까지 빼기 진행하기
        result += (n-1)
        
        print(result)
        ```