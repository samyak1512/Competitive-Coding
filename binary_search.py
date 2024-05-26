low = 0
high = n-1
target = k

ans = 0
while low <= high:
    mid = low + (high - low)//2
    if arr[mid] == target:
        # ans = mid
        break
    if arr[mid] < target:
        ans = mid
        low =  mid + 1
    if arr[mid] > target:
        # ans = mid
        high = mid - 1

