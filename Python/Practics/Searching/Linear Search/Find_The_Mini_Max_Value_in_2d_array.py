import sys
def find_mini_value(arr):
    if len(arr) == 0:
        return "Null"

    miniElement = sys.maxsize + 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < miniElement:
                miniElement = arr[i][j]
    return "Minimum Eliment in The 2d Array: ", miniElement
    
def find_max_value(arr):
    if len(arr) == 0:
        return "Null"
    
    maxElement = -sys.maxsize - 1
    # return maxElement
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > maxElement:
                maxElement = arr[i][j]
    return "Maxim Eliment in The 2d Array: ", maxElement

nums = [
        [1, -56, 20, 38],
        [48, 7, -96],
        [ 7, 8, -9, 0],
        [1, 2, -99],
        [8, 400]
        ]

print(find_mini_value(nums))
print(find_max_value(nums))