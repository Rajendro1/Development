def find_mini_value(arr):
    if len(arr) == 0:
        return "Null"
    
    ans = arr[0]
    for i in range(len(arr)):
        if arr[i] < ans:
            ans = arr[i]
    return ans
    
def find_max_value(arr):
    if len(arr) == 0:
        return "Null"
    
    ans = arr[0]
    for i in range(len(arr)):
        if arr[i] > ans:
            ans = arr[i]
    return ans

nums = [1, 20, 38, -20, -48, 65, 96, 7, 8, -999, 0,]

print(find_mini_value(nums))
print(find_max_value(nums))