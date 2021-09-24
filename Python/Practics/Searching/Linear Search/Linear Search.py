def linear_search(arr, target):
    if len(arr) == 0:
        return -1
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return "Don't Find This Value In This Array"


nums = [1, 20, 38, 48, 65, 96, 7, 8, 9, 0,]

#  Taking String
# nums_s1 = "rajendro"

# String Convert To Array
# str12 = list(nums_s1)
# print(str1)

# Find The Element Of The Array
target_value = 65

print(linear_search(nums, target_value))




