---

## 정렬

- 정렬 : 데이터를 특정한 기준에 따라서 순서대로 나열
- 오름차순 정렬 후, 내림차순이 필요한 경우 O(N) 복잡도의 뒤집기 실행

### (1) 선택 정렬

- `가장 작은 것을 선택해서 앞으로 보내는 과정을 반복`해 정렬
- 복잡도 : `O(N^2)` → 비효율적
- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 다음 작은 데이터를 두번째와 바꾸고, … 반복
    
    ![2024-03-11_03-22-00.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/abc3c425-0915-4608-8ed5-c2548a5fcf5c/2024-03-11_03-22-00.jpg)
    
    ![2024-03-11_03-22-13.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/243b3d06-741a-4d67-a6be-b6f7fbe0a89a/2024-03-11_03-22-13.jpg)
    
- 코드
    
    ```python
    for i in range(len(array)):
    		min_index = i
    		for j in range(i+1, len(array)):
    				if (array[min_index] > array[j]):
    						min_index = j
    		array[i], array[min_index] = array[min_index], array[i]
    ```
    

### (2) 삽입 정렬

- `특정한 데이터를 순서에 맞게 적절한 위치에 삽입`해 정렬
- 필요할 때에만 위치를 수정함 → 데이터가 거의 정렬이 되어있을 때 특히 효과적
    - 복잡도 : `O(N^2)`, but 최상의 경우 복잡도 : `O(N)`
- 2번째 원소부터, 정렬된 원소들과 비교해보며 위치 찾아서 삽입 진행
    
    ![2024-03-11_04-21-03.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/cad69e1d-e45c-4062-9095-ccc673430ba2/2024-03-11_04-21-03.jpg)
    
- 코드
    - 정렬된 원소들 중, 가장 마지막 인덱스의 원소부터 하나하나 비교해보며 위치 찾아감
    
    ```python
    # 첫번째 원소 제외 N-1 번 반복 실행
    for i in range(1, len(array)):
    		for j in range(i, 0, -1):
    				if (array[j] < array[j - 1]):
    						array[j], array[j - 1] = array[j - 1], array[j]
    				else :
    						break
    ```
    

### (3) 퀵 정렬

- 가장 많이 활용되는 정렬
- `기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈`
- 복잡도 : `O(NlogN)`
- 호어 분할 방식
    - 리스트의 첫 데이터를 `피벗`(기준)으로 설정
    - 왼쪽에서 피벗보다 큰 데이터를, 오른쪽에서 피벗보다 작은 데이터를 찾아 위치 교환
    
    ![2024-03-11_04-44-52.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/4f595351-8320-4995-b3c9-4bb40a466d9f/2024-03-11_04-44-52.jpg)
    
    ![2024-03-11_04-45-09.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/a7b74077-7988-41d8-8af7-68b09203d6fa/2024-03-11_04-45-09.jpg)
    
    ![2024-03-11_04-45-33.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/cc2ed11b-a1a8-4f3b-823f-741eef9d4bed/2024-03-11_04-45-33.jpg)
    
    결과 :
    
    ![2024-03-11_05-03-48.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/73d5edc0-d184-4c0d-b9f4-162c6c9c06ae/2024-03-11_05-03-48.jpg)
    
- 코드로 구현 :
    
    ```python
    def quick_sort(array, start, end):
    		if (start >= end) :
    				return
    		pivot = start
    		left = start + 1
    		right = end
    		
    		while (left <= right) :
    				while (left <= end and array[left] <= array[pivot]):
    						left += 1
    				while (right > start and array[right] >= array[pivot]):
    						right -= 1
    						
    				if (left < right) :
    						array[left], array[right] = array[right], array[left]
    				else :
    						array[right], array[pivot] = array[pivot], array[right]
    						
    		quick_sort(array, start, right-1)
    		quick_sort(array, right+1, end)
    		
    quich_sort(array, 0, len(array)-1)
    print(array)
    ```
    
- 파이썬 라이브러리를 활용하는 경우 :
    
    ```python
    def quich_sort(array):
    		if (len(array) <= 1) :
    				return array
    		
    		pivot = array[0] # 피벗
    		tail = array[1:] # 피벗을 제외한 리스트
    		
    		left_side = [x for x in tail if x <= pivot]
    		right_side = [x for x in tail if x > pivot]
    		
    		return quich_sort(left_side) + [pivot] + quich_sort(right_side)
    ```
    

### (4) 계수 정렬

- 특정 조건을 만족해야만 사용 가능하지만, 매우 빠른 알고리즘
- `데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때` 사용 가능
- 복잡도 : `O(N+K)`
- 일반적으로 데이터 크기만큼의 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담음
    
    ![2024-03-11_05-46-20.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/0a1ecf3e-8fa9-4361-b3b0-204fe5e3b3c1/2024-03-11_05-46-20.jpg)
    
    ![2024-03-11_05-46-31.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/9cd39722-394d-46cc-9b40-1d3a1797fc60/2024-03-11_05-46-31.jpg)
    
    ![2024-03-11_05-46-48.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/351d55c0-0149-47d3-a465-0f3f917087bd/2024-03-11_05-46-48.jpg)
    
- 코드 :
    
    ```python
    count = [0] * (max(array) + 1)
    
    # 각 데이터에 해당하는 인덱스 값 증가
    for i in range(len(array)):
    		count [array[i]] += 1
    
    # 리스트에 기록된 정렬 정보 호가인 후 횟수만큼 출력
    for i in range(len(count)):
    		for j in range(count[i]):
    				print(i, end='')
    ```
    

### (5) 파이썬 기본 라이브러리 활용

- `sorted()` : 병합 정렬(퀵정렬과 유사) 기반 → `O(NlogN)` 복잡도 보장
- 활용 :
    
    ```python
    result = sorted(array)
    print(result)
    ```
    
    ```python
    array.sort()
    print(array)
    ```
    
- 매개변수 활용:
    
    ```python
    array = [("나",2), ("가",1), ("다",3)]
    
    def setting(data):
    		return data[1]
    
    result = sorted(array, key=setting)
    print(result)
    ```
    
    ```python
    result = sorted(array, key=lambda data: data[1])
    print(result)
    ```
    

## 2. 학생 성적순으로 정렬하기

 

<aside>
❔ N명의 학생 정보가 이름, 성적으로 구분되어 존재한다.

각 학생의 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하시오.

</aside>

![2024-03-12_02-39-05.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/94106562-4628-421c-8477-cb722e5b39b0/2024-03-12_02-39-05.jpg)

- 풀이
    
    ```python
    # 학생 수 입력받기
    n = int(input())
    
    # N명의 학생을 입력받고 리스트에 저장하기
    array = []
    for i in range(n) :
        input_data = input().split()
        array.append(input_data[0],int(input_data[1]))
    
    # key를 활용해 정수 값을 기준으로 정렬하기
    array = sorted(array, key=lambda student: student[1])
    
    # 정렬된 순서로 출력
    for student in array:
        print(student[0], end='')
    ```
    

## 3. 두 배열의 원소 교체하기

<aside>
❔ N개의 자연수 원소로 구성된 배열 A와 B가 있으며,

최대 K번의 바꿔치기 연산을 통해 배열 A의 모든 원소의 합이 최대가 되도록 하시오.

(1 ≤ N ≤ 100000, 0 ≤ K ≤ N)

</aside>

![2024-03-12_07-59-44.jpg](https://prod-files-secure.s3.us-west-2.amazonaws.com/edfd69d1-6c01-4d0c-9269-1bae8a4e3915/2b0f826a-d383-4c8e-aaff-4d164a08d23a/2024-03-12_07-59-44.jpg)

- 풀이
    - A에서 가장 작은 원소를, B에서 가장 큰 원소를 고를 후 비교해서 작으면 교체, 최대 K번 반복
    
    ```python
    # N, K 입력받기
    n, k = map(int, input().split())
    
    # A, B 배열 입력받기
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # 오름차순, 내림차순 진행
    a.sort()
    b.sort(reverse=True)
    
    # 최대 K번 비교 진행
    for i in range(k) :
        if (a[i] < b[i]) :
            a[i], b[i] = b[i], a[i]
        else :
            break
    
    print(sum(a))
    ```