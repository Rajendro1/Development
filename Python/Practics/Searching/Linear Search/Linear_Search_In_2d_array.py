def linear_search_2d(arr, target):
    if len(arr) == 0:
        return -1
    
    for row in range(len(arr)):
        # Here length of arr[row] important Because after this statement the loop itarate
        # end of the first row 
        for element in range (len(arr[row])):
            if arr[row][element] == target:
                return row, element,

    return "Don't Find This Value In This Array"


nums = [
        [1, -56, 20, 38],
        [ 48, 65, -96],
        [ 7, 8, -9, 0]
        ]
#  Taking String
# nums_s1 = "rajendro"

# String Convert To Array
# str12 = list(nums_s1)
# print(str1)

# Find The Element Of The Array
target_value = -96

print(linear_search_2d(nums, target_value))
