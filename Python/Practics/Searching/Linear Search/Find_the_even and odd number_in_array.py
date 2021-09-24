def cheacking_number(arr):
    if len(arr) == 0:
        return "Nul"

def even_number(arr):
    # cheacking_number(arr)
    numberofdigits = digits(arr)
    return numberofdigits % 2 == 0
    # for i in range(len(arr)):
    #     if arr[i] % 2 == 0:
    #         print(arr[i], end=" ")

def odd_number(arr):
    cheacking_number(arr)

    count = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            count += 1
            print(arr[i], end=" ")

def digits(num): 
    count = 0 
    while(num > 0):
        count += 1
        num /= 10

def find_numbers(number):
    count = 0
    for i in number:
        if even_number(number):
            count += 1
    return count

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    # print(even_number(nums))
    # print(odd_number(nums))
    print(find_numbers(nums))

