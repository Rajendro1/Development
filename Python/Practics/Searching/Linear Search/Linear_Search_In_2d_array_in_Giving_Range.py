# WRONG MODIFIY IT LATER

def linear_search_2d_by_range(arr, target):
    if len(arr) == 0:
        return -1
    # r, y, z = arr[1][0], arr[3][0], len(arr)

    # for i in range(arr[1][0], arr[3][0]):
    #     print(i)
    # return r, y, z
    for i in range(arr[1], arr[3]):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return i, j
    
    return "Don't Find This Value In This Given Range Of Array"


nums = [
        [1, -56, 20, 38],
        [48, 65, -96],
        [ 7, 8, -9, 0],
        [1, 2, 9],
        [8, 4]
        ]


# Find The Element Of The Array
target_value = 8

print(linear_search_2d_by_range(nums, target_value))
#  Taking String
# nums_s1 = "rajendro"

# String Convert To Array
# str12 = list(nums_s1)
# print(str1)

