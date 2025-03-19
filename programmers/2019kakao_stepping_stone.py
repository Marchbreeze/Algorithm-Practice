def solution(stones, k):
    answer = 0
    start = 1
    end = 200000000
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for stone in stones:
            if (stone - mid <= 0):
                count += 1
            else:
                count = 0
            if (count >= k):
                answer = mid
                end = mid - 1
                break
        else:
            start = mid + 1
    
    return answer