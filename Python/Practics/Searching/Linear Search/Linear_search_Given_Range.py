def liner_serch_byrange(arr, target, start, end):
    if len(arr) == 0:
        return "Null Index"
    
    for i in range(start, end):
        if arr[i] == target:
            return i
    return "Don't Find The Value In The Given Range"


nums = [1, 20, 38, 48, 65, 96, 7, 8, 9, 0,]

#  Taking String
# nums_s1 = "rajendro"

# String Convert To Array
# str12 = list(nums_s1)
# print(str1)

# Find The Element Of The Array
target_value = 65

# We Give Start To End List Index Number
print(liner_serch_byrange(nums, target_value, 2, 6))