---

## 이진 탐색

- `순차 탐색`
    - 리스트 안에 있는 특정 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
    - 보통 정렬되지 않은 리스트에서 데이터를 찾아야할 때, 시간이 충분하다면 활용
    - 리스트 자료형 중 count()도 순차 탐색 활용됨
    - 최악의 시간 복잡도 `O(N)`

- `이진 탐색`
    - 배열 내부의 데이터가 `정렬되어 있을 때` 사용 가능
    - 이미 정렬되어 있는 경우, 빠르게 데이터를 탐색할 수 있음
    - 시간 복잡도 : `O(logN)`

### 이진 탐색 방법

- 이진 탐색 방법 :
    - 탐색 범위를 절반씩 좁혀가며 탐색
    - 변수 3개를 활용함 : `시작점`, `끝점`, `중간점`
    - 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 탐색
    
    ![2024-03-12_16-33-35.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/2fb9fda7-9e6e-4d88-a8cc-efe5d4ef1731/2024-03-12_16-33-35.jpg)
    
    ![2024-03-12_16-34-10.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/8bd3f3f8-14bc-4209-9eaa-437e4f55a729/2024-03-12_16-34-10.jpg)
    

- 재귀함수 활용 코드 :
    
    ```python
    def binary_search(array, target, start, end):
    		if (start > end) :
    				return None
    		mid = (start + end) // 2
    		if (array[mid] == target) :
    				return mid
    		elif (array[mid] > target) :
    				return binary_search(array, target, start, mid-1)
    		else :
    				return binary_search(array, target, mid+1, end)
    				
    # 에시
    result = binary_search(array, target, 0, n-1)
    if (result == None) :
    		print("원소가 존재하지 않습니다")
    else :
    		print(result + 1)
    ```
    

### 이진 탐색 트리

- `왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드` 가 성립하는 이진 트리
- 이진 탐색 트리가 구현된 경우, 데이터 조회가 용이함
- 탐색 방법 :
    
    ![2024-03-12_17-02-50.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/480f51c9-6859-4141-90ac-788efb5a101e/2024-03-12_17-02-50.jpg)
    
    ![2024-03-12_17-03-28.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/8ec57d2e-649d-4b5c-9be6-14fba14efaf7/2024-03-12_17-03-28.jpg)
    

### readline() 활용하기

- 이진 탐색 문제 : 일반적으로 입력 데이터 값이 많거나 탐색 범위가 넓음
    - 데이터 개수가 `1000만개` 이상 or 탐색 범위 `1000억` 이상
- input() 함수는 동작 속도가 느림
    
    → `sys 라이브러리의 readline() 함수` 활용
    

- 예시 :
    
    ```python
    import sys
    
    input_data = sys.stdin.readline().rstrip()
    ```
    
    - 한 줄 입력 받고 나서 rstrip() 호출 필요함
        
        (엔터를 줄 바꿈 기호로 인식해 공백 문자로 되지 않도록 함)
        

## 2. 부품찾기

<aside>
❔ 가게에 정수 형태의 고유번호를 가진 부품 N개가 있다.

손님이 M개 종류의 부품을 구매하고자 할때, 가게에 모든 부품이 있는지 확인하는 프로그램을 작성해보자.

(1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 100,000)

</aside>

![2024-03-12_17-13-36.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/e1f23d39-05c1-468f-bb66-ce6155d28c32/2024-03-12_17-13-36.jpg)

- 이진 탐색 풀이
    - 정렬된 가계 상품 내역에서, 고객의 주문을 하나씩 이진 탐색으로 확인
    
    ```python
    # 이진 탐색 소스코드
    def binary_search(array, target, start, end):
    		if (start > end) :
    				return None
    		mid = (start + end) // 2
    		if (array[mid] == target) :
    				return mid
    		elif (array[mid] > target) :
    				return binary_search(array, target, start, mid-1)
    		else :
    				return binary_search(array, target, mid+1, end)
    		
    # 상점 입력값 입력
    n = int(input())
    storeList = list(map(int, input().split()))
    storeList.sort()
    
    # 고객 입력값 입력
    m = int(input())
    buyList = list(map(int, input().split()))
    
    # 고객의 부품 번호를 하나씩 확인
    for i in buyList :
    	result = binary_search(storeList, i, 0, n-1)
    	if (result != None) :
    		print('yes', end='')
    	else :
    		print('no', end='')
    ```
    

- 계수 정렬 풀이
    - 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 생성한 다음
    - 리스트의 인덱스에 직접 접근하여 특정 번호가 존재하는지 확인
    
    ```python
    # 가게 부품 입력받기
    n = int(input())
    
    # 가게의 전체 부품 리스트에 입력받기
    array = [0] * 100001
    for i in input().split():
        array[int(i)] = 1
    
    # 고객의 부품 입력받기
    m = int(input())
    buyList = list(map(int, input().split()))
    
    # 고객의 부품 하나씩 확인하기
    for i in buyList :
        if array[i] == 1:
           print('yes', end='')
        else :
            print('no', end='')
    ```
    
- 집합 자료형 이용 풀이
    - 단순히 특정 수가 한 번이라도 등장했는지를 검사하면 됨 → 집합 자료형 활용
    - `set()` 함수는 집합 자료형을 초기화할 때 활용함
    
    ```python
    # 상점 입력값 입력
    n = int(input())
    storeList = set(map(int, input().split()))
    
    # 고객 입력값 입력
    m = int(input())
    buyList = list(map(int, input().split()))
    
    # 고객의 부품 번호를 하나씩 확인
    for i in buyList :
    	if (i in storeList) :
    		print('yes', end='')
    	else :
    		print('no', end='')
    ```
    

## 3. 떡 높이 맞춰 자르기

<aside>
❔ 총 길이가 정수인 떡을 일정한 높이 H로 자른다.

높이가 H보다 긴 떡을 H보다 긴 부분들이 잘릴 것이다.

N개의 떡이 있을 때, 손님은 모든 잘린 부분을 가져간다.

손님이 적어도 총 길이 M의 떡을 가지고 가려할 때, 절단기의 높이 H의 최댓값을 구하시오.

(1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000, 1 ≤ H ≤ 10억)

</aside>

- `파라메트릭 서치` 유형의 문제
    - 최적화 문제를 결정 문제(Y/N)로 바꾸어 해결하는 기법
    - ‘원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제’에 자주 활용됨
    - 일반적으로 이진 탐색 유형을 활용해 해결함
- 풀이
    - 절단기 높이 H를 반복해서 조정해가며 조건 만족 여부 확인 → 탐색 범위 좁혀나가기
    - H ≤ 10억 → `큰수를 보면 이진 탐색`을 떠올려야 함 (순차 탐색의 경우 연산 횟수 초과)
        - 근데,,, 어처피 N의 크기에 따라야 하는거 아닌가,,,?
    
    ![2024-03-13_02-37-34.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/5829e954-0059-4301-9727-31bdecf0d990/2024-03-13_02-37-34.jpg)
    
    ```python
    # 떡 개수와 필요 길이, 개별 높이 입력
    n, m = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    # 이진 탐색 점 설정
    start = 0
    end = max(array)
    
    # 이진 탐색 수행 (반복적)
    result = 0
    while (start <= end) :
        total = 0
        mid = (start + end) // 2
        for x in array:
            if (x > mid) :
                total += x - mid
        # 부족한경우 더 많이 자르기 (왼쪽 부분탐색)
        if (total < m) :
            end = mid - 1
        # 충분한경우 더 조금 자르기 (오른쪽 부분탐색)
        else :
            result = mid
            start = mid + 1
    
    print(result)
    ```