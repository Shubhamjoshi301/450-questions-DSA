def max_sub_array_sum(arr):
    max_so_far, local_max = -float("inf"),0
    for i in range(len(arr)):
        local_max = max(arr[i],local_max+arr[i])
        max_so_far = max(max_so_far,local_max)
        
    return max_so_far


arr = list(map(int,input().split(',')))
print(max_sub_array_sum(arr))