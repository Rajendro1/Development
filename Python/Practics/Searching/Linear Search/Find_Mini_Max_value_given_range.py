def find_mini_value_range(arr, start, end):
    if len(arr) == 0:
        return "Null"

    ans = arr[0]
    for i in range(start, end):
        if arr[i] < ans:
            ans = arr[i]
    return ans

def find_max_value_range(arr, start, end):
    if len(arr) == 0:
        return "Null"
    
    ans = arr[0]
    for i in range(start, end):
        if arr[i] > ans:
            ans = arr[i]
    return ans

nums = [1, 20, 38, -20, -48, 65, 96, 7, 8, -999, 0,]

print(find_mini_value_range(nums, 3, 10))
print(find_max_value_range(nums, 1, 5))